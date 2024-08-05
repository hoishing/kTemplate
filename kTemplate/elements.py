"""create tagged element functions for common elements

non-common or custom elements can be created by `element` function in main.py

pre created tagged element functions are:
a,
article,
aside,
audio,
b,
base,
blockquote,
body,
br,
button,
canvas,
caption,
cite,
code,
col,
colgroup,
data,
dd,
div,
dl,
dt,
em,
fieldset,
figcaption,
figure,
figure,
footer,
frame,
frameset,
h1,
h2,
h3,
h4,
h5,
h6,
head,
header,
hr,
html,
i,
iframe,
img,
input,
label,
legend,
li,
link,
main,
menu,
meta,
nav,
object,
ol,
option,
p,
param,
picture,
pre,
q,
script,
section,
select,
small,
source,
span,
strongtable,
style,
sub,
sup,
tbody,
td,
template,
textarea,
tfoot,
th,
thead,
timeform,
title,
tr,
track,
ul,
video
"""

from .main import create_elements


DOCTYPE = "<!DOCTYPE html>"
"""HTML5 preamble"""

[
    a,
    article,
    aside,
    audio,
    b,
    core,
    blockquote,
    body,
    br,
    button,
    canvas,
    caption,
    cite,
    code,
    col,
    colgroup,
    data,
    dd,
    div,
    dl,
    dt,
    em,
    fieldset,
    figcaption,
    figure,
    figure,
    footer,
    frame,
    frameset,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    head,
    header,
    hr,
    html,
    i,
    iframe,
    img,
    input,
    label,
    legend,
    li,
    link,
    main,
    menu,
    meta,
    nav,
    object,
    ol,
    option,
    p,
    param,
    picture,
    pre,
    q,
    script,
    section,
    select,
    small,
    source,
    span,
    strongtable,
    style,
    sub,
    sup,
    table,
    tbody,
    td,
    template,
    textarea,
    tfoot,
    th,
    thead,
    timeform,
    title,
    tr,
    track,
    ul,
    video,
] = create_elements(
    """
    a,
    article,
    aside,
    audio,
    b,
    base,
    blockquote,
    body,
    br,
    button,
    canvas,
    caption,
    cite,
    code,
    col,
    colgroup,
    data,
    dd,
    div,
    dl,
    dt,
    em,
    fieldset,
    figcaption,
    figure,
    figure,
    footer,
    frame,
    frameset,
    h1,
    h2,
    h3,
    h4,
    h5,
    h6,
    head,
    header,
    hr,
    html,
    i,
    iframe,
    img,
    input,
    label,
    legend,
    li,
    link,
    main,
    menu,
    meta,
    nav,
    object,
    ol,
    option,
    p,
    param,
    picture,
    pre,
    q,
    script,
    section,
    select,
    small,
    source,
    span,
    strongtable,
    style,
    sub,
    sup,
    table,
    tbody,
    td,
    template,
    textarea,
    tfoot,
    th,
    thead,
    timeform,
    title,
    tr,
    track,
    ul,
    video
"""
)