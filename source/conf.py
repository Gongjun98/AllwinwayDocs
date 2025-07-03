# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

source_encoding = 'utf-8-sig'
project = 'AllwinwayDocs'
copyright = '2025, Allwinway'
author = 'Allwinway'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

#extensions = ['myst_parser','sphinx_markdown_tables']
extensions = [
    'myst_parser',
    'sphinx_markdown_tables'
    #"sphinxcontrib.mermaid",
    #"sphinx_copybutton",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "tasklist",
    "deflist",
    "dollarmath",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']

import sys
print(sys.executable)
