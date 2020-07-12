#!/usr/bin/env python3

import base64
import random
import sys
import os

OCTICONS_REPO = "https://github.com/primer/octicons.git"
ICON_PATH = "/icons"
OUT_PATH = "/_octicons"

MD_TEMPLATE = """---
icon_id: {icon_id}
name: {name}
icon_16: {icon_16}
icon_24: {icon_24}
---
"""

OVERRIDES = {
    # icon_id => name to replace automatic name
    "mark-github": "GitHub Logo",
}

# Step 1: Clone the octicons to a random temporary directory.
tmpdir = "/tmp/octicons-{}".format(int(random.random() * 1e8))
repodir = os.getcwd()

if repodir.endswith("/scripts"):  # remove suffix
    repodir = repodir[:-8]

os.system("git clone {} {}".format(OCTICONS_REPO, tmpdir))
os.chdir(tmpdir + ICON_PATH)

# Step 2: Make a map of all icons.


class Icon:
    def __init__(self, icon_id, name):
        self.icon_id = icon_id
        self.name = name if icon_id not in OVERRIDES else OVERRIDES[icon_id]
        self.svg_16 = "null"
        self.svg_24 = "null"

    def encode_icon(self, svg_data):
        svg_bytes = svg_data.encode("utf-8")
        return base64.b64encode(svg_bytes).decode("ascii")

    def set_16(self, svg_16):
        self.svg_16 = self.encode_icon(svg_16)

    def set_24(self, svg_24):
        self.svg_24 = self.encode_icon(svg_24)

    def to_markdown(self):
        return MD_TEMPLATE.format(
            icon_id=self.icon_id,
            name=self.name,
            icon_16=self.svg_16,
            icon_24=self.svg_24,
        )


icons = {}

for filename in os.listdir("."):
    with open(filename, "r") as f:
        icon_id = filename[:-7]
        size = filename[-6:-4]
        svg_data = f.read()

        if icon_id not in icons:
            name = icon_id.replace("-", " ").title()
            icons[icon_id] = Icon(icon_id, name)

        if size == "16":
            icons[icon_id].set_16(svg_data)
        elif size == "24":
            icons[icon_id].set_24(svg_data)
        else:
            raise Exception('Unexpected size: "{}"'.format(size))

# Step 3: create Jekyll collection with the icon data.
os.chdir(repodir + OUT_PATH)
os.system("rm *.md")

for filename, icon in icons.items():
    with open(filename + ".md", "w") as f:
        f.write(icon.to_markdown())
