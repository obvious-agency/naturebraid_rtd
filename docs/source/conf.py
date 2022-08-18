# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Nature Braid Documentation'
copyright = '2022, Nature Braid'
author = 'Nature Braid team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_wagtail_theme', 'myst_parser']

templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_wagtail_theme'
html_static_path = ['_static']
html_css_files = ["css/custom.css"]

html_theme_options = dict(
    project_name = "Nature Braid documentation",
    logo = "img/luci-logo-transparent.png",
    logo_alt = "Nature Braid",
    logo_height = 59,
    logo_url = "/",
    logo_width = 45,
    github_url = "",
    header_links = "",
    footer_links = ",".join([
        "About Us|https://naturebraid.org/about",
        "Contact|https://naturebraid.org/contact",
    ]),
)

html_show_copyright = False
