# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
import sys, os
sys.path.append(os.path.abspath('../../src'))
sys.path.append(os.path.abspath('../../src/structinator'))
sys.path.append(os.path.abspath('../../src/structinator/data'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Structinator'
copyright = '2023, Joseph Laccone'
author = 'Joseph Laccone'
release = '0.0.2'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode"
]

viewcode_line_numbers = True

templates_path = ['_templates']
exclude_patterns = []
#include_patterns = ['./data']
#source_suffix = ['.xml']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_theme_options = {
    "sidebarwidth": "30%"
}
html_static_path = ['_static']
