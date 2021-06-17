# flask-api-template

![Python CI](https://github.com/DiljotSG/flask-api-template/workflows/Python%20application/badge.svg?branch=master)

This repository provides the basic tools for creating a Python REST API powered by [Flask](https://flask.palletsprojects.com/en/1.1.x/).

# Setup

This codebase uses Python3.7.X/Python3.8.X. These setup instructions are for macOS using [Homebrew](https://brew.sh).

Installing these dependencies should be similar for other platforms with the appropriate package managers for that platform.

## Python3 Installation

1. Install python.

    ```shell
    brew install python
    sudo pip3 install virtualenv
    ```

## Environment Setup

These steps are required for development.

1. Create a Python virtual environment.

    ```shell
    virtualenv -p python3 venv
    ```

2. Activate the environment.

    ```shell
    . venv/bin/activate
    ```

3. Install Python dependencies.

    ```shell
    pip3 install -r requirements.txt
    ```

4. Run the flask application locally.

    ```shell
    python3 index.py
    ```

    Development Mode (Auto reloads on code changes):

    ```shell
    export FLASK_ENV=development

    python3 index.py
    ```

# Testing

You can quickly and easily run all the unit tests locally on your machine with the following command.

```shell
python -m unittest discover tests
```
