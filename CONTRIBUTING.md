# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Environment setup

install [poetry](https://python-poetry.org/) if you haven't.

Fork and clone the repository, then:

```shell
cd kTemplate
poetry install --with dev
```

You now have the dependencies installed in `.venv` folder.

## Development

1. start the environment with `poetry shell`
1. create a new branch: `git checkout -b feature-or-bugfix-name`
1. edit the code and/or the documentation
1. test your code with `coverage run -m pytest --doctest-modules kTemplate tests`

### Code Formatting

- run `black kTemplate/ tests/` to auto-format the code
- or in vscode use `black` as the python auto formatter

### Testing

This package primarily use `doctest` in docstring to perform simple unit tests,
as well as creating documentation in one go.
For more complicated tests that require setup / teardown,
and parameterized input, `pytest` is recommended.

Please test the code and fix any issue before making PR.

### Updating Docs

If you updated the docs:

- run `mkdocs serve`
- visit http://localhost:8000 and check that everything looks good

## CI - Github Action

If you are unsure about how to fix the error/warning from github action,
just let the continuous integration fail,
and we will help you during review.

Don't bother updating the changelog, we will take care of this.
