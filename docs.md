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

This option may be set on a per-import level basis as well (see the
[classes parameter docs](#classes)).

## Usage

To add an icon, simply write a Liquid include like the example below:

<!-- {% raw %} -->

```html
{% include octicon icon_id="alert" size="16" %}
```

<!-- {% endraw %} -->

Simply substitute the desired `icon_id` and `size` to create the icon you want.

### **Parameter** `icon_id`

This parameter is **required**.

The full catalog of available icons and their associated `icon_id`s are
available at the [icon gallery page](icons.html).

### **Parameter** `size`

This parameter is **required**.

The upstream Octicons repository only has assets for 16x and 24x icons, thus the
only legal values for `size` are `"16"` or `"24"`.

### **Parameter** `classes`

This parameter is **_optional_**.

You may optionally supply a classlist to be applied to the icon that is inserted
onto your page. Multiple classes may be applied by adding a space between them.

Supplying parameter only affects the current import. To set this globally,
see the [configuration options](#configuration).

If the global classlist is set also, the two classlists are concatenated and the
global classlist will be placed before the import-level classlist.
