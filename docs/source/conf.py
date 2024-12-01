# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Document Q&A System'
copyright = '2024, Nada'
author = 'Nada'

release = '1.0'
version = '1.0.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'myst_parser',  # Add MyST parser for markdown support
]

# Intersphinx mappings
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Path to templates (optional)
templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
html_theme = 'material'

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'

# -- MyST-specific configuration --------------------------------------------
# Enable markdown extensions for MyST parsing
myst_enable_extensions = [
    'amsmath',  # Example: If you want to enable LaTeX math
    'dollarmath',  # For inline math support
    'deflist',  # For definition lists
    'linkify',  # To automatically convert URLs to links
]

# If you're using markdown, ensure the source is pointing to your markdown files
source_suffix = ['.rst', '.md']  # Allow both .rst and .md files
