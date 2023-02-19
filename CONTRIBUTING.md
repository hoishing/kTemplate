# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Environment setup

- install [poetry](https://python-poetry.org/)
- fork the repo to your github account
- clone the repo and change into the directory
- install the dependencies:

```shell
poetry install --with dev
```

Dev dependencies are installed in `.venv` folder.

## Development

1. start the environment with `poetry shell`
1. create a new branch: `git checkout -b branch-name`
1. edit the code and docs
1. test your code with `pytest --doctest-modules path/to/your/files`

### Code Formatting

- run `black path/to/your/files` to auto-format the code
- or use `black` as the python auto formatter in your code editor

### Testing

This package use both `doctest` in docstring and `pytest` to perform tests.
Please test the code and fix any issue before making PR.

### Updating Docs

If you updated the docs:

- run `mkdocs serve`
- visit http://localhost:8000 and check that everything looks good

## CI - Github Action

If you are unsure about how to fix the error/warning from github action,
just let the CI fail, we will help you during code review.

Don't bother updating the changelog, we will take care of this.
