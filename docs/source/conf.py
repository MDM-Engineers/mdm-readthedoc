# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MDM Engineering'
copyright = '2025, MDM Engineers'
author = 'Phu, Thien'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = "shibuya"

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Localization configuration

locale_dirs = ['locale/']  # Path to translation files
gettext_compact = False  # Use separate .po files for each document

# -- Language configuration

language = 'en'  # Default language

# -- Customization for multiple languages

# html_context = {
#     'languages': [
#         ("English", "/%s/", 'en')
#     ],
# }
# Customizing the theme options
# This is where you can set theme-specific options

html_theme_options = {
    "accent_color": "blue",
    "github_url": "https://github.com/MDM-Engineers/mdm-readthedoc",

    "globaltoc_expand_depth": 1,
    "nav_links": [
        {
            "title": "Platforms",
            "children": [
                {
                    "title": "Jamf MDM",
                    "url": "jamf/index",
                    "summary": "Management of Apple devices by Jamf",
                },
                {
                    "title": "Intune MDM",
                    "url": "intune/index",
                    "summary": "Microsoft MDM solution",
                },
            ]
        },
        {
            "title": "About us",
            "url": "about/index",
            "summary": "Learn more about MDM Engineers",           
        },
        
    ]
}