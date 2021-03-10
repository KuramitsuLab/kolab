# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Python & Data Science 2021'
copyright = '2021, 倉光君郎(Kimio Kuramitsu)'
author = 'Kimio Kuramitsu'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
]

exclude_patterns = ['_build', '**.ipynb_checkpoints']

source_suffix = ['.rst', '.md']

# source_parsers = {
#    '.md': CommonMarkParser,
# }

github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'


def setup(app):
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
    }, True)
    app.add_transform(AutoStructify)

# Add any paths that contain templates here, relative to this directory.


templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

nbsphinx_allow_errors = True
nbsphinx_execute = 'never'
