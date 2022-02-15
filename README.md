# lifespline-praxis-template-python

Python template for the `lifespline-praxis` service.

# Getting started

+ Create a [circleci](https://circleci.com/) account to host the CICD pipeline for your python package.
+ Create a [github](https://github.com/) account and an organization `{org-name}`. Grant `{org-name}` oAuth to the circleci app.
+ Create a [dockerhub](https://hub.docker.com/) account to host the python image that will execute your [circleci](https://circleci.com/) CICD pipeline.
+ Create a development deployment environment for your package in [testpypi]() and get the API token `{testpypi-api-token}`
+ Create a production deployment environment for your package in [pypi]() and get the API token `{pypi-api-token}`
+ Fork this repository in github as `{fork-name}`
+ Clone `{fork-name}` locally
+ Initalize a virtual environment with all the dependencies installed:
    ```sh
    {fork-name} . bootstrap.sh
    [testpypi-api-token] {testpypi-api-token}
    [pypi-api-token] {pypi-api-token}
    ```
+ Confirm your identity:
    ```bash
    git config user.name {your-username}
    git config user.email {your-useremail}
    ```
+ Prepare the build and publishing of your python package from the template by:
    ```bash
    # building and publishing the circleci python docker executor
    docker build . \
       -t {your-dockerhub}/{your-dockerhub-repo}:{your-dockerhub-tag} \
       -f .circleci/python_executor.Dockerfile
    docker push {your-dockerhub}/{your-dockerhub-repo}:{your-dockerhub-tag}

    # main and dev don't allow pushes
    git checkout -b tmp
    git commit --allow-empty -m "build and push package"
    git push --set-upstream origin tmp
    ```
+ Publish the python package by issuing a PR from tmp to dev, and from dev to main.
+ Overwrite files or replace `lifespline-praxis-template-python` with your own package name:
    + `LICENSE`
    + `README.md`
    + `setup.py`
    + `test/*`
    + `src/*`
    + `doc/*`

Congratulations, your python template was successfuly built and published. You are free to begin coding!
