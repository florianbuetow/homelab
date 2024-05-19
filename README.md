# HomeLab

A bunch of useful tools and scripts to manage my home lab of Raspberri Pis

## Contents

```text

├── README.md
├── src
│   ├── recipes
│   │   ├── Recipe.py             - Base class for all recipes
│   │   ├── Recipes.py            - Where the actual recipes are defined
│   ├── setup_new_pi.py                 - Current script to setup a new Raspberry Pi
│   └── util
│       ├── ConnectionManager.py        - Helper to establish SSH connections and execute commands on a remote host
│       ├── TemplateHelper.py           - Helper class to manage templates
└── templates
    ├── raspbian-bullseye_base.template       Base template to configure a new Raspberry Pi running Raspbian Bullseye 
    └── raspbian-bullseye_k3.template         Template to install k3s on a Raspberry Pi with Raspbian Bullseye

```
