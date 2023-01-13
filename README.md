# kTemplate

[![GitHub](https://img.shields.io/github/license/hoishing/kTemplate)](https://opensource.org/licenses/MIT)

> a minimalist python html template lib

## Why? [![start with why](https://img.shields.io/badge/start%20with-why%3F-brightgreen.svg?style=flat)][start-with-why]

When building web apps with python, no matter using which framework, Flask, FastAPI, Django...etc. The go-to template is [Jinja][jinja]. In many cases, using Jinja for simple web app is just over-kill. Also, I am not the fan of its template syntax, I feel a bit clumsy putting python  loops in html with `{% ... %}` like this:

```html
<ul id="navigation">
{% for item in navigation %}
    <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
{% endfor %}
</ul>
```

in contrast, I prefer something like this:

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

Its pure python, having full support of intellisense, type checking, and all language supports from the IDE / text editor. So in general I feel better DX with this approach.

Separation of concern sounds good, but it comes with a cost of adding an extra layer of concern, ie. complexity. So separating HTML with python is not always a good choice. That's why people invented JSX in javascript, or prefer Tailwind over separate CSS file.

Mixing template logic within python reduces that layer of complexity, which I think is a reasonable choice for small/medium size projects. There are libs provide html template within python, such as [Dominate][dominate] and [fast-html][fast-html].

Dominate is a well designed lib and I'll certainly go for it for medium sized project. Their `with element_name` pattern is a brilliant use of python context manager, highly recommended 👍 However, for small project, I still looking for a simpler solution.

fast-html come close to what I want. It uses python `generator` as element output to speed up the template concatenation process. This is a efficient technical choice, and I think that's why the author name it "fast" html. But still, when dealing with small or even single page demo sites, pure text elements is what I am looking for instead of generator. Performance hit of pure text manipulation in small projects is negligible.

Thats why I create this text centric html template lib and share it on PyPi. I name it "k" template after my name, that is 😜. Hope u find it useful.

🔗 [source code](https://github.com/hoishing/kTemplate)

## Usage

### Installation

`pip install kTemplate`

Pure python package, zero dependency.

### Tagged Element Functions

- common elements(div, span, a, img ...etc) can be imported directly

    eg. `#!py from kTemplate import div, span, a, img`

- see list of common elements [here][common]
- rare or custom element could be created by the `element` function

    eg. `#!py element(tag='MyTag', content='foo', href='bar')`

    → `#!html <MyTag href="bar">foo</MyTag>`

### Element Function Arguments

#### content

- `content=None`, which is the default value, create void element.

    void element examples: br, hr, img, meta ... etc

    eg. `br()` → `#!html <br />`

- empty string `content=""` creates element with end tag without content.

    eg `content=script(content="")` → `<o></script>`

- can mix other elements with text.

    eg. `content=f"this {i('is')} good"` →  `#!html this <i>is</i> good`

- use `list` to create multiple child elements

    eg. `div(content=[br(), hr()])` → `#!html <div><br /><hr /></div>`

#### **attrs

- string, included empty string `""` create string attributes
- non-string truthy value create empty attribute

    eg. `#!py option("foo", selected=True)` -> `#!py <option selected>foo</option>`

- attribute is omitted for non-string falsy value(`None`, `False`, `[]`, `0` ...etc)

    eg. `#!py option("bar", selected=False)` -> `#!py <option>bar</option>`

### Example

The following example demonstrate the key features provided by kTemplate. See [References](./reference.md) for full documentation.

```python
from kTemplate import (
    DOCTYPE,  # special non-element
    html,
    div,
    img,
    body,
    head,
    title,
    script,
    select,
    option,
)
from kTemplate import element  # for creating custom element


html_str = DOCTYPE + html(
    [
        head(
            # use list to enclose multiple siblings
            [
                title("testing html template"),
                
                # attr=True will convert to attribute w/o value, eg. defer
                script(
                    src="https://cdn.jsdelivr.net/npm/@unocss/runtime/attributify.global.js",
                    defer=True
                ),
            ]
        ),
        body(
            [
                # content-less element without closing tag
                img(src="http://placekitten.com/150/100"),

                # cls attribute will convert to `class`
                div("pls select the direction:", cls="text-xl"),
                select(
                    # attr selected showup when selected=True, otherwise omitted
                    [
                      option(dir, selected=(dir == "South"))
                      for dir in "East South West North".split()
                    ]
                    # underscore will convert to hyphen, eg. `data-type`
                    data_type="direction"  
                ),

                # create custom element
                element(tag="MyElement", props="some-props")
            ],
            cls="font-sans",
        ),
    ]
)
```

Note that in order to workaround python naming constrains:

- `class` attribute denoted by `cls`
- underscore `_` will be converted to hyphen `-`

## Contribution

Contributions are welcome, note that:

- we use [Black](https://black.readthedocs.io) as the code formatter
- we use [Poetry][poetry] for package management
- please make sure all tests below are passed before making pull requests

## Testing

- fork [kTemplate](https://github.com/hoishing/kTemplate)
- install [Poetry][poetry]

```bash
# install dev dependencies
poetry install

# activate dev env in sub shell
poetry shell

# run the test and generate coverage info
coverage run -m pytest tests/

# view coverage report
coverage report
```

## Need Help?

Open a [github issue](https://github.com/hoishing/kTemplate/issues) or ping me on [Twitter](https://twitter.com/hoishing) ![](https://api.iconify.design/logos/twitter.svg?width=20)

[poetry]: https://python-poetry.org/docs/
[jinja]: https://jinja.palletsprojects.com
[fast-html]: https://pypi.org/project/fast-html
[dominate]: https://pypi.org/project/dominate
[common]: https://github.com/hoishing/kTemplate/blob/main/kTemplate/elements.py
[start-with-why]: https://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action
