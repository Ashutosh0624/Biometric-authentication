# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Biometric authentication using Facial recognition'
copyright = '2025, Ashutosh Kumar Tiwari'
author = 'Ashutosh Kumar Tiwari'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.bibtex',  # Enable bibliography support
    'sphinx.ext.mathjax',
]

bibtex_bibfiles = ['references.bib']  # Path to the .bib file with your references

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


# -- Options for LaTeX output ------------------------------------------------
# Settings for generating the paper in IEEE format

latex_engine = 'xelatex'

latex_elements = {
    'preamble': r'''
    \documentclass[conference]{IEEEtran}
    \usepackage{amsmath}
    \usepackage{graphicx}
    \usepackage{float}
    ''',
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'figure_align': 'H',
}



# Optionally set a title for the generated LaTeX file
latex_documents = [
    ('index', 'BiometricAuthentication.tex', 'Biometric Authentication using Facial Recognition',
     'Ashutosh Kumar Tiwari', 'manual'),
]
