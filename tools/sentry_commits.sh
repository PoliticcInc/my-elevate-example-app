#!/bin/sh

set -e

echo "TRAVIS_COMMIT: $TRAVIS_COMMIT"
echo "TRAVIS_COMMIT_RANGE: $TRAVIS_COMMIT_RANGE"

if [[ ! "$TRAVIS_COMMIT" ]] && [[ -n "$TRAVIS_COMMIT_RANGE" ]]; then
	  echo "Missing environment variable: TRAVIS_COMMIT or TRAVIS_COMMIT_RANGE"
	  exit 1
fi

for commit in $(git rev-list --reverse $TRAVIS_COMMIT_RANGE)
do
    sentry-cli releases --org=$SENTRY_ORG --project=$SENTRY_PROJECT set-commits $TRAVIS_COMMIT --commit lululemon/ecom-web-app@$commit
done
