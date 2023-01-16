# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.1.0](https://github.com/hoshing/kTemplate/releases/tag/0.1.0) - 2023-01-14

<small>[Compare with first commit](https://github.com/hoishing/kTemplate/commit/6431e04e8662ae19b3a8d2ea60c8784fcc2e4346...0.1.0)</small>

### Added

- kTemplate core features
  - element function
  - common tagged elements
- tests
  - parasitized pytest
  - doctest in docstring
- documentation
  - docstring in Google format
  - detail examples
  - README with quick start
  - changelog
  - contributing guideline
- mkdocs setup
  - dark and light theme
  - snippets: importing other files into mkdocs
- CD/CI with github actions on push
  - run pytest
  - run doctest
  - generate function reference from docstring with [mkdocstings](https://github.com/mkdocstrings/mkdocstrings)
  - deploy mkdocs
