# kTemplate

[![ci-badge]][ci-url] [![pypi-badge]][pypi-url] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

> a minimalist python html template

- [docs]

## Quick Start

### Installation

`pip install kTemplate`

### Examples

```python
from kTemplate import (
  div, img, # common html elements
  element   # for creating custom element
)

# create common html element
# `class` represents by `cls` due to python keyword
html_str = div(img(src='url'), cls='bar')
# <div class="bar"><img src="url"/></div>

# create custom element
my_element = element(tag="MyElement", content="foo" props="bar")
# <MyElement props="ar">foo</MyElement>
```

see also: how to create [templates and components]

## Motivation

When creating simple website, instead of seperating python and template files like this:

```html
<ul id="navigation">
  {% for item in navigation %}
  <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
  {% endfor %}
</ul>
```

I prefer a pure python approach like this:

```python
ul(
  id = "navigation",
  content = [
    li(
      a(item.caption, href=item.href)
    )
    for item in navigation
  ]
)
```

It provides full intellisense, type checking, and all language supports from the text editor. I feel a better DX with this approach.

## Need Help?

Open a [github issue] or ping me on [Twitter ![twitter-icon]][Twitter]

[github issue]: https://github.com/hoishing/kTemplate/issues
[Twitter]: https://twitter.com/hoishing
[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20
[ci-badge]: https://github.com/hoishing/kTemplate/actions/workflows/ci.yml/badge.svg
[ci-url]: https://github.com/hoishing/kTemplate/actions/workflows/ci.yml
[MIT-badge]: https://img.shields.io/github/license/hoishing/kTemplate
[MIT-url]: https://opensource.org/licenses/MIT
[pypi-badge]: https://img.shields.io/pypi/v/ktemplate
[pypi-url]: https://pypi.org/project/ktemplate/
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-url]: https://github.com/psf/black
[templates and components]: https://hoishing.github.io/kTemplate/usage/#templates-and-components
[docs]: https://hoishing.github.io/kTemplate
