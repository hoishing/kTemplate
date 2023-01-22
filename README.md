# kTemplate

[![ci-badge]][ci-url] [![coverage-badge]][coverage-url] [![pypi-badge]][pypi-url] [![py-version]][py-url] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

> a minimalist python html template

## Quick Start

### Installation

`pip install kTemplate`

### Example

```python
from kTemplate import (
  div, img, # common html elements
  element   # for creating custom element
)

# create common html element
# `class` represents by `cls` due to python keyword
html_str = div(img(src='url'), cls='bar')
# -> <div class="bar"><img src="url"/></div>

# create custom element
my_element = element(tag="MyElement", content="foo" props="bar")
# -> <MyElement props="ar">foo</MyElement>
```

## Documentation

Please refer the [docs] for more about:

- [why] creating this package
- [usage] details
- function [references]
- [contributing] guideline
- [testing]
- [changelog]

## Need Help?

Open a [github issue](https://github.com/hoishing/kTemplate/issues) or ping me on [Twitter](https://twitter.com/hoishing) ![](https://api.iconify.design/logos/twitter.svg?width=20)

[ci-badge]: https://github.com/hoishing/kTemplate/actions/workflows/ci.yml/badge.svg
[ci-url]: https://github.com/hoishing/kTemplate/actions/workflows/ci.yml
[coverage-badge]: https://hoishing.github.io/kTemplate/assets/coverage-badge.svg
[coverage-url]: https://hoishing.github.io/kTemplate/assets/coverage/
[MIT-badge]: https://img.shields.io/github/license/hoishing/kTemplate
[MIT-url]: https://opensource.org/licenses/MIT
[pypi-badge]: https://img.shields.io/pypi/v/ktemplate
[pypi-url]: https://pypi.org/project/ktemplate/
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[py-version]: https://img.shields.io/pypi/pyversions/kTemplate
[py-url]: https://python.org
[docs]: https://hoishing.github.io/kTemplate/
[why]: https://hoishing.github.io/kTemplate/why
[usage]: https://hoishing.github.io/kTemplate/usage
[references]: https://hoishing.github.io/kTemplate/ref
[contributing]: https://hoishing.github.io/kTemplate/contribute/
[testing]: https://hoishing.github.io/kTemplate/contribute#testing
[changelog]: https://hoishing.github.io/kTemplate/changelog
