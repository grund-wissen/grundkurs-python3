import sys, os

sys.path.append(os.path.abspath('_exts'))

extensions = [ 
    'matplotlib.sphinxext.mathmpl',
    'matplotlib.sphinxext.only_directives',
    'matplotlib.sphinxext.plot_directive',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo', 
    'sphinx.ext.coverage', 
    'sphinx.ext.pngmath',
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
project = 'Scipy- und Sympy'
html_short_title  = 'Scipy und Sympy'
htmlhelp_basename = 'Scipy und Sympy'

version = '0.0.1'
release = '0.0.1'
copyright = '2014, Bernhard Grotz'
language = 'de'
spelling_lang = 'de_DE'
pygments_style = 'sphinx'
html_theme = 'sphinxdoc'
html_logo = "logo.png"
html_favicon = "favicon.ico"
html_static_path = ['_static']
html_last_updated_fmt = '%d. %b %Y'
html_use_smartypants = True
html_additional_pages = {'home': 'home.html'}
html_domain_indices = False
html_use_index = True

html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = False


# latex_logo = "logo.png"

latex_preamble = r'''
\usepackage[version=3]{mhchem}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb, color, xlop}
\usepackage{nicefrac,marvosym,mathtools,wasysym} 
\setcounter{secnumdepth}{-1}
\setlength{\headheight}{15pt}
\setcounter{tocdepth}{2}
'''

latex_show_pagerefs    = True
pngmath_latex_preamble = latex_preamble

latex_elements = {
    "preamble": latex_preamble,
    "babel": "\\usepackage[ngerman]{babel}",
    "classoptions": 'oneside,openany',    
    "papersize": 'a4paper',
    "pointsize": '12pt',
    "fontpkg": '',
    "fncychap": '\\usepackage[Conny]{fncychap}'
}

latex_domain_indices = False



latex_show_pagerefs = True

latex_documents = [
   ('index', 'tutorial-scipy-sympy.tex', 'Tutorial: Scipy und Sympy',
   'Bernhard Grotz', 'manual'),
]

man_pages = [
    ('index', 'tutorial-scipy-sympy', 'Tutorial: Scipy und Sympy',
     ['Bernhard Grotz'], 1)
]


