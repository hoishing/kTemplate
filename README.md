# kTemplate

[![ci-badge]][ci-url] [![coverage-badge]][coverage-url] [![pypi-badge]][pypi-url] [![py-version]][py-url] [![MIT-badge]][MIT-url] [![black-badge]][black-url]

> a minimalist python html template

🔗 [source code]

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

Please refer to the docs for creating HTML [templates and components]

## Documentation

Read the [documentation] for more about:

- usage details
- function references
- contributing
- testing
- changelog

## Motivation

When building web apps with python, no matter using Flask, FastAPI or Django, the go-to template is [Jinja]. This is a sensible choice when building web app. However it's a bit over-kill when creating simple website. Also, I am not a fan of Jinja's template syntax, eg. putting python loops in html with `{% ... %}` looks clumsy:

```html
<ul id="navigation">
{% for item in navigation %}
    <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
{% endfor %}
</ul>
```

I prefer something like this instead:

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

Its pure python, having full support of intellisense, type checking, and all language supports from the text editor. I feel much better DX with this approach.

Separation of concern sounds good, but it comes with a cost: adding another concern 🤪... So separating HTML with python is not always a good choice, especially in simple projects.

Mixing template logic within python eliminates the extra layer of complexity, which I think is a reasonable choice for small/medium size projects. There are libraries provide in-python html template, such as [Dominate] and [fast-html].

Dominate is a well designed lib and I'll certainly go for it for medium sized project. Their `with element_name` pattern is a brilliant use of python context manager, highly recommended 👍. However, for simple project, I'm still looking for a simpler solution.

`fast-html` come close to what I want. It uses python `generator` as element output to speed up the template concatenation process. This is a efficient technical choice, and I think that's why the author name it "fast" html. But still, when dealing with simple or even single page demo sites, pure text elements is what I am looking for instead of generator. Performance hit is negligible in that case.

That's why I create this text centric html template library, and share it on PyPi. I name it "k" template because... just after my initial 😜. Hope u find it useful.

[Jinja]: https://jinja.palletsprojects.com
[fast-html]: https://pypi.org/project/fast-html
[Dominate]: https://pypi.org/project/dominate

## Need Help?

Open a [github issue] or ping me on [Twitter ![twitter-icon]][Twitter]

[github issue]: https://github.com/hoishing/kTemplate/issues
[Twitter]: https://twitter.com/hoishing
[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20
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
[documentation]: https://hoishing.github.io/kTemplate/
[templates and components]: https://hoishing.github.io/kTemplate/usage/#templates-and-components
[source code]: https://github.com/hoishing/kTemplate
