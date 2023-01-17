# Contributing

Contributions are welcome, and they are greatly appreciated!
Every little bit helps, and credit will always be given.

## Environment setup

install [poetry](https://python-poetry.org/) if you haven't.

Fork and clone the repository, then:

```bash
cd kTemplate
poetry install --with test --with docs
```

You now have the dependencies installed in `.venv` folder.

## Development

1. start the environment with `poetry shell`
1. create a new branch: `git checkout -b feature-or-bugfix-name`
1. edit the code and/or the documentation

### Code Formatting

- run `black kTemplate/ tests/` to auto-format the code
- or in vscode use `black` as the python auto formatter

### Testing

This package primarily use `doctest` in docstring to perform unit tests,
as well as providing usage examples. For tests require setup / teardown,
and parameterized input, `pytest` can be used.
Please run `pytest --doctest-modules`
to test the code and fix any issue before submit.

### Updating Docs

If you updated the docs:

- run `mkdocs serve`
- visit http://localhost:8000 and check that everything looks good

## CI - Github Action

If you are unsure about how to fix the error/warning from github action,
just let the continuous integration fail,
and we will help you during review.

Don't bother updating the changelog, we will take care of this.
