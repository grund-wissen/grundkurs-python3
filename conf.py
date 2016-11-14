import sys, os

sys.path.append(os.path.abspath('_exts'))

extensions = [
    # 'matplotlib.sphinxext.mathmpl',
    # 'matplotlib.sphinxext.only_directives',
    # 'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    # "sphinxcontrib.blockdiag",
    # "sphinxcontrib.seqdiag",
]


# 'ipython_console_highlighting',
# 'inheritance_diagram',
# 'numpydoc', 'lily',

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Grundkurs Python 3'
htmlhelp_basename = 'Grundkurs Python 3'
html_short_title  = 'Grundkurs Python 3'

version = '0.1.1a'
release = '0.1.1a'
copyright = '2014-2016, Bernhard Grotz'
language = 'de'
spelling_lang = 'de_DE'
pygments_style = 'sphinx'
html_theme = 'sphinxdoc'
html_logo = "logo.png"
html_favicon = "favicon.ico"
html_static_path = ['_static']
html_last_updated_fmt = '%d.%m.%Y'
today_fmt = '%d.%m.%Y'

html_use_smartypants = True
html_additional_pages = {'home': 'home.html'}
html_domain_indices = False
html_use_index = True

html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False
html_search_language = 'en'
html_search_options = {'type': 'default'}

exclude_patterns = ["notes.rst", "*/notes.rst",
                    "**/notes.rst","todos.rst","README.rst"]

# latex_logo = "logo.png"

latex_preamble = r'''
\usepackage[version=3]{mhchem}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb, color}
\usepackage{nicefrac,marvosym,mathtools,wasysym}
\setcounter{secnumdepth}{-1}
\setlength{\headheight}{15pt}
\setcounter{tocdepth}{1}
'''

imgmath_latex_preamble = latex_preamble

latex_elements = {
    "preamble":     latex_preamble,
    "babel":        "\\usepackage[ngerman]{babel}",
    "classoptions": 'oneside,openany,',
    "papersize":    'a4paper,',
    "pointsize":    '12pt,',
    "fontpkg":      '',
    "fncychap":     ''
}

# "fncychap":     '\\usepackage[Conny]{fncychap}'
latex_domain_indices = False


# latex_show_pagerefs    = True


latex_documents = [
   ('index', 'grundkurs-python3.tex', 'Grundkurs Python 3',
   'Bernhard Grotz', 'manual'),
]

intersphinx_mapping = {
    'gw':   ('http://grund-wissen.de/', None),
    'gwm':  ('http://grund-wissen.de/mathematik/', None),
    'gwp':  ('http://grund-wissen.de/physik/', None),
    'gwe':  ('http://grund-wissen.de/elektronik/', None),
    'gwl':  ('http://grund-wissen.de/linux/', None),
    'gwic': ('http://grund-wissen.de/informatik/c', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
}

