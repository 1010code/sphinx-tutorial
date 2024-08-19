# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-tutorial'
copyright = '2024, andy6804tw'
author = 'andy6804tw'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


latex_engine = 'xelatex'
latex_elements = {
  'papersize': 'a4paper',
  'pointsize': '12pt',
  'preamble': r'''
\usepackage[UTF8]{ctex}
​
\setCJKmainfont[BoldFont=STZhongsong, ItalicFont=STKaiti]{STSong}
\setCJKsansfont[BoldFont=STHeiti]{STXihei}
\setCJKmonofont{STFangsong}
\XeTexlinebreaklocale "zh"
\XeTexlinebreakskip = Opt plus 1pt
\parindent 2em
\definecolor (VerbatimColor}{rgb}{0.95,0.95,0.95)
\setcounter{tocdepth}{3} \renewcommand\familydefault{\ttdefault}
\renewcommand\CJKfamilydefault{\CJKrmdefault}
​
''',
}