# kTemplate

[![GitHub](https://img.shields.io/github/license/hoishing/kTemplate)](https://opensource.org/licenses/MIT)

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

Please refer the [docs](https://hoishing.github.io/kTemplate) for more about:

- why creating this package
- usage details
- function references
- contributing guideline
- testing
- changelog

## Need Help?

Open a [github issue](https://github.com/hoishing/kTemplate/issues) or ping me on [Twitter](https://twitter.com/hoishing) ![](https://api.iconify.design/logos/twitter.svg?width=20)
