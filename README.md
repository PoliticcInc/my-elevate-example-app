
<p align="center">
  <img alt="ecom-npp-web-app" src="https://user-images.githubusercontent.com/423755/28759078-4ca94672-754d-11e7-9fb3-1e2dcaea6492.png" width="308">

</p>

<p align="center">
lululemon e-commerce north america post purchase web app
</p>
<p align="center">
  <a href="http://standardjs.com/"><img  src="https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat-square"></a>
  <a href="http://standardjs.com/"><img  src="	https://img.shields.io/github/downloads/atom/atom/latest/total.svg"></a>
  <a href="https://npmjs.org/package/ecom-npp-web-app"><img alt="npm version" src="http://img.shields.io/npm/v/ecom-npp-web-app.svg?style=flat-square"></a>
  <a href="https://npmjs.org/package/ecom-npp-web-app"><img alt="npm version" src="http://img.shields.io/npm/dm/ecom-npp-web-app.svg?style=flat-square"></a>
  <a href="https://github.com/lululemon/ecom-npp-web-app/pulls?q=is%3Apr+is%3Aclosed"><img alt="PR Stats" src="https://img.shields.io/issuestats/i/github/lululemon/ecom-npp-web-app.svg?style=flat-square"></a>
  <a href="https://github.com/lululemon/ecom-npp-web-app/issues?q=is%3Aissue+is%3Aclosed"><img alt="Issue Stats" src="https://img.shields.io/issuestats/p/github/lululemon/ecom-npp-web-app.svg" style=flat-square"></a>
 <a><img  src="https://img.shields.io/github/forks/lululemon/ecom-npp-web-app.svg"/></a>
 <a><img  src="https://img.shields.io/github/stars/lululemon/ecom-npp-web-app.svg"/></a>
 <a><img  src="https://img.shields.io/badge/license-MIT-blue.svg"/>

 

<h4 align="center">A progressive web application built on <a href="https://reactjs.org/">React</a></h4>

<p align="center">
 <a href="https://codeclimate.com/repos/59ee6140cf0a7202c6000349/maintainability"><img src="https://api.codeclimate.com/v1/badges/30ae005d6ba6a6b8901c/maintainability" /></a>
 <a href="https://travis-ci.com/Lululemon/ecom-npp-web-app"><img src="https://travis-ci.com/Lululemon/ecom-npp-web-app.svg?token=rcNZwgCUqW1TW7SP8YTQ&branch=master" alt="Build Status"></a>
 <a href="https://codecov.io/gh/Lululemon/ecom-npp-web-app"><img src="https://codecov.io/gh/Lululemon/ecom-npp-web-app/branch/master/graph/badge.svg?token=mmBCXJEjUE" alt="Codecov" /></a>
</p>

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](https://git-scm.com/)
* [Node.js](https://nodejs.org/) (with [Yarn](https://yarnpkg.com))
  * Prefer nodejs version [8.10.x](https://nodejs.org/download/) as mandated by the AWS Lamda [execution environment](http://docs.aws.amazon.com/lambda/latest/dg/current-supported-versions.html)
  * Prefer Yarn

### Recommended IDE / Editor Extensions

* Wallaby - https://marketplace.visualstudio.com/items?itemName=WallabyJs.wallaby-vscode


### Preparing your workstation (MacOS)
* Set up your [Github SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)


## Installation

Clone repository
* `git clone git@github.com:Lululemon/ecom-npp-web-app.git` this repository
* `cd ecom-npp-web-app`

Install dependencies
* `yarn install`


### Runtime Configuration

During development your local code will use the file located at `env.json` for loading runtime configuration. This file is not tracked and so changes will not be shared with any other development environment.


## Running / Development

* `yarn dev`
* Visit your app at [http://localhost:3000](http://localhost:3000)

### Running Tests

Before running tests, run `yarn dev` to compile locally.

`yarn test`


## Contribution Guide

Please follow our [JavaScript Style Guide](https://github.com/Lululemon/javascript-style-guide)
