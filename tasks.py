from invoke import task
from os import environ
import os
from sys import exit
import subprocess
import shutil
import glob
import boto3
import json
import yaml

def sanity_check(ctx):
    if environ.get('ARTIFACT_DEPLOY_REGION') is None:
        exit("Environment variable ARTIFACT_DEPLOY_REGION not set")
    ctx.travis_pull_request = environ.get('TRAVIS_PULL_REQUEST')
    if ctx.travis_pull_request is None or ctx.travis_pull_request == 'false':
        print("NOT a pull request")
        if environ.get('TRAVIS_BRANCH') == 'master':
            ctx.travis_pull_request = 'master'
        else:
            exit(0)
    else:
        print("Found pull request number via environment variable: [TRAVIS_PULL_REQUEST={}]".format(
            ctx.travis_pull_request))


def init(ctx):
    ctx.artifact_deploy_region = environ.get('ARTIFACT_DEPLOY_REGION', 'us-west-2')
    ctx.github_base_url = "https://github.com"
    ctx.travis_base_url = "https://travis-ci.com"

    ctx.build_dir = 'embed'


def distribute(ctx, name, env_name=None, tag=None):
    # NOTE: all TRAVIS_* vars exist in the travisCI build environment
    travis_repo_slug = environ.get('TRAVIS_REPO_SLUG', '')
    travis_commit_range = environ.get('TRAVIS_COMMIT_RANGE', '')
    travis_build_id = environ.get('TRAVIS_BUILD_ID', '')
    travis_job_number = environ.get('TRAVIS_JOB_NUMBER', '')
    travis_node_version = environ.get('TRAVIS_NODE_VERSION', '')
    travis_commit = environ.get('TRAVIS_COMMIT', '');

    target_branch = environ.get('TRAVIS_BRANCH', '')


    meta_data = {
        'pr_number': ctx.travis_pull_request,
        'git_diff_url': '{}/{}/compare/{}'.format(ctx.github_base_url, travis_repo_slug, travis_commit_range),
        'pr_url': '{}/{}/pull/{}'.format(ctx.github_base_url, travis_repo_slug, ctx.travis_pull_request),
        'ci_build_url': '{}/{}/builds/{}'.format(ctx.travis_base_url, travis_repo_slug, travis_build_id),
        'ci_build_number': travis_job_number,
        'ci_build_lang_version': travis_node_version
    }


        # We will s3 sync all build assets to this folder
    if env_name:
        artifact_builds_s3_object_folder = "ecom/client/embed/environments/{}/{}/{}".format(env_name, name, tag)
    else:
        tag = 'master' if ctx.travis_pull_request == 'master' else 'pr-{}'.format(ctx.travis_pull_request)
        artifact_builds_s3_object_folder = "ecom/client/embed/distributions/{}/{}".format(name, tag)

    # NOTE: all TRAVIS_* vars exist in the travisCI build environment
    travis_repo_slug = environ.get('TRAVIS_REPO_SLUG', '')
    travis_commit_range = environ.get('TRAVIS_COMMIT_RANGE', '')
    travis_commit = environ.get('TRAVIS_COMMIT', '');
    travis_pull_request = environ.get('TRAVIS_PULL_REQUEST', '')
    travis_build_id = environ.get('TRAVIS_BUILD_ID', '')
    travis_job_number = environ.get('TRAVIS_JOB_NUMBER', '')
    travis_node_version = environ.get('TRAVIS_NODE_VERSION', '')

    meta_data_elements = [
        'pr_number={}'.format(ctx.travis_pull_request),
        'git_diff_url={}/{}/compare/{}'.format(ctx.github_base_url, travis_repo_slug, travis_commit_range),
        'pr_url={}/{}/pull/{}'.format(ctx.github_base_url, travis_repo_slug, travis_pull_request),
        'ci_build_url={}/{}/builds/{}'.format(ctx.travis_base_url, travis_repo_slug, travis_build_id),
        'ci_build_number={}'.format(travis_job_number),
        'ci_build_lang_version={}'.format(travis_node_version)
    ]

    with open('./{}/index.js'.format(ctx.build_dir), 'r') as index_file:
        index_file = index_file.read()
        index_file_data = index_file.decode('utf-8')
    s3_client = boto3.client('s3')

    s3_client.put_object(
        Body=bytes(index_file_data.encode('utf-8')),
        Key='{}/{}.js'.format(artifact_builds_s3_object_folder, ctx.rev),
        Bucket=ctx.artifact_deploy_s3_bucket, Metadata=meta_data
    )

    s3_client.put_object(
        Body=bytes(ctx.rev.encode('utf-8')),
        Key='{}/latest'.format(artifact_builds_s3_object_folder),
        Bucket=ctx.artifact_deploy_s3_bucket, Metadata=meta_data
    )

    s3_client.put_object(
        Body=bytes(target_branch.encode('utf-8')),
        Key='{}/branch'.format(artifact_builds_s3_object_folder),
        Bucket=ctx.artifact_deploy_s3_bucket, Metadata=meta_data
    )
    




@task()
def package(ctx):
    """
    Packaging consists of:

    1. Building the web app
    3. Compress all of the files from the web app build
    5. Distribute the web app to the client builds bucket location

     The result is that the following artifacts / files will be in S3:

     contents of `./build/` will be synced to:

     lll-testing-static-clients/ecom/client/<path>/distributions/my-elevate-example-app/pr-<PR_NUMBER>

    :return:
    """
    """ We use the current commit's short SHA1 fingerprint to name the artifact. """
    ctx.rev = ctx.run('git rev-parse --short HEAD').stdout.strip()

    """ Perform sanity check to make sure that we can build safely and that we have some build related env vars set. """
    sanity_check(ctx)
    init(ctx)

    """ Now we distribute the web app and create a sentry release"""
    ctx.artifact_deploy_s3_bucket = 'lll-testing-static-clients'
    distribute(ctx, 'my-elevate-example-app')
