---
title: Docs
---

# Documentation

Using `octicons-jekyll-include` on your site is easy to do.

## Requirements

`octicons-jekyll-include` is designed to work with any recent version of Jekyll.

Since it requires no plugins to work, it also works on GitHub Pages! Even if
your site is hosted elsewhere, it should still work.

## Installation

Copy the following files to your site:

- the `_octicons` directory and its contents
- `_includes/octicon`

## Configuration

There is only one global configuration option: `octicons_classes`.

This optional value may be set in `_config.yml` to specify which classes
should be appended to any icon added to your pages.

It should be either a classlist **string** or `null`. Multiple classes may be
applied by placing a space between them.

This option may be set on a per-import level basis as well (see the
[classes parameter docs](#classes)).

## Usage

To add an icon, simply write a Liquid include like the example below:

<!-- {% raw %} -->

```html
{% include octicon id="alert" size="16" %}
```

<!-- {% endraw %} -->

Simply substitute the desired icon `id` and `size` to create the icon you want.

### **Parameter** `id`

This parameter is **required**.

The full catalog of available icons and their associated `id`s are
available at the [icon gallery page][icon-gallery].

### **Parameter** `size`

This parameter is **required**.

The upstream Octicons repository only has assets for 16x and 24x icons, thus the
only legal values for `size` are `"16"` or `"24"`.

### **Parameter** `classes`

This parameter is **_optional_**.

You may optionally supply a classlist to be applied to the icon that is inserted
onto your page. Multiple classes may be applied by adding a space between them.

For example, this import applies the `d-block` and `mb-2` classes:

<!-- {% raw %} -->

```html
{% include octicon id="bell" size="24" classes="d-block mb-2" %}
```

<!-- {% endraw %} -->

Supplying parameter only affects the current import. To set this globally,
see the [configuration options](#configuration).

If the global classlist is set also, the two classlists are concatenated and the
global classlist will be placed before the import-level classlist.

## Troubleshooting

If an icon appears on your page as a broken image like the one below, you will
need to check the developer console of your browser.

{% include octicon id="nonexistent icon" size="24" %}

The octicons include provides hints as to what went wrong with an import
at the end of the `src` attribute for the image.

For example, you might see this:

```html
<img
  src="data:image/svg+xml;base64,ERROR MESSAGE HERE"
  class="octicon octicon-24"
/>
```

You can try this by using the web inspector to view the broken icon above.

The error message values are described below.

### Error 1: `unknown error`

It should be theoretically impossible to get this error. If you
do, please [file a ticket][new-ticket].

### Error 2: `bad icon size`

This error occurs when the specified size is not exactly either `"16"` or
`"24"`. For more details, see the [size parameter](#parameter-size).

### Error 3: `size not available: {size}`

This error occurs when the icon `id` and `size` have valid values, but the
icon is not available in the size requested.

_Not all icons will have both sizes!_

Check the entry for your icon in the [icon gallery][icon-gallery] to see what
sizes are available for the icon you want.

### Error 4: `bad icon id`

This error occurs when the icon `id` does not match any of the icons present in
the `_octicons` folder.

Keep in mind that while the filenames do match the icon `id`, the `icon_id`
field in the front matter of each file is what will actually be used to identify
the icon on include!

Check the [icon gallery][icon-gallery] for a list of valid icon `id`s.

[new-ticket]: https://github.com/BenJetson/octicons-jekyll-include/issues/new
[icon-gallery]: {{site.url}}{{site.baseurl}}/icons
