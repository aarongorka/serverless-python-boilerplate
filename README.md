# Serverless Python Boilerplate

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), this is a template for deploying Python 3.6 Lambdas using the [Serverless](https://github.com/serverless/serverless) framework.

## Features
  * Log shipping powered by [serverless-log-forwarding](https://github.com/amplify-education/serverless-log-forwarding) to ship logs to Sumo Logic
  * Monitoring powered by [serverless-plugin-aws-alerts](https://github.com/ACloudGuru/serverless-plugin-aws-alerts) using CloudWatch metrics
  * JSON formatted logging powered by [aws_lambda_logging](https://gitlab.com/hadrien/aws_lambda_logging) including correlation IDs and `LOGLEVEL` settings
  * Dependency management with `pip` and [requirements.txt]({{cookiecutter.project_slug}}/requirements.txt)
  * The ability to invoke your Lambda locally powered by [docker-lambda](https://github.com/lambci/docker-lambda/)
  * Docker, docker-compose and make as the only dependencies required to deploy

## Usage
You can either use `cookiecutter` by installing it with `pip`, or running it in Docker.
## pip
`pip install cookiecutter`
## Docker
Using [docker-cookiecutter](https://github.com/amaysim-au/docker-cookiecutter), alias `cookiecutter` in your `~/.bashrc`:
```bash
alias cookiecutter='docker run --rm -it --user $(id -u):$(id -g) -v $(pwd):/srv/app:Z -v ${HOME}/.ssh:/home/cookiecutter/.ssh:Z amaysim/cookiecutter:1.5.1'
```
## Cloning
Once you have `cookiecutter` installed, clone the template and follow the prompts:
```bash
cookiecutter git@github.com:amaysim-au/serverless-python-boilerplate.git
```

## Contributing
You can test any changes you make by using the [Makefile](Makefile) in this repo.

To create a test project from the template:
```bash
make clone
```
To run a full end-to-end test on the test project, fill out the required variables `.env` file under `python-test-project/.env` and run:
```bash
make recursive
```
This will invoke an e2e test on the template, involving building a package, running a style check, invoking it locally, deploying it, invoking it remotely and finally removing it.
