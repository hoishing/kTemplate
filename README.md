# kTemplate

[![GitHub](https://img.shields.io/github/license/hoishing/kTemplate)](https://opensource.org/licenses/MIT)

> a minimalist python html template lib

## Why

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

## Technical Details

🔗 [source code](https://github.com/hoishing/kTemplate)

### Install

`pip install kTemplate`

Pure python package, zero dependency.

### Usage

- [common elements][common] can be imported directly
- rare or custom element could be created by the `element` method

#### element function arguments

- content  
  - `None` for content-less "void" element. eg. br, img
  - empty string "" for element with end tag but no content. eg script
  - string to put in the content of element, can mix with other elements. eg. `this <i>is</i> good`
  - list of string: put multiple child elements inside an element
- attributes
  - string, included empty string "" output as attribute string value
  - boolean `True` produce attribute without value. eg. `defer=True` -> `defer`
  - attribute is omitted for non-string or non `True` value, eg. None, int, float...etc

### Example

This example demonstrate all features provided by kTemplate.

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

### Test

- install pytest
  - with poetry config in this repo `poetry install`

- run the test
  - start python env in sub shell `poetry shell`
  - run the tests `pytest -v`

## Need Help?

Open a [github issue](https://github.com/hoishing/kTemplate/issues) or ping me on [Twitter](https://twitter.com/hoishing) ![](https://api.iconify.design/logos/twitter.svg?width=20)

[jinja]: https://jinja.palletsprojects.com
[fast-html]: https://pypi.org/project/fast-html
[dominate]: https://pypi.org/project/dominate
[common]: https://https://github.com/hoishing/kTemplate
