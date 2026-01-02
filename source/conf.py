# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#import sphinx_rtd_theme

project = 'SGL'
copyright = '2026, SGL All contributors'
author = 'SGL Team'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = [
#         'sphinx_togglebutton',
#         'myst_parser',
#         'sphinx_copybutton',
#         'sphinx_markdown_tables',
#         'sphinxemoji.sphinxemoji',
# ]

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "classic"
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = []
