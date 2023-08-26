# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'BEND'
copyright = '2023, F.I. Marin, F. Teufel, M. Horlacher, D. Pultz, O. Winther, W. Boomsma'
author = 'F.I. Marin, F. Teufel, M. Horlacher, D. Pultz, O. Winther, W. Boomsma'
release = '0.1.0'


import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.coverage',
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
