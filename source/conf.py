# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'AllwinwayDocs'
copyright = '2025, Allwinway'
author = 'Allwinway'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    #from convert_readme import convert_md
    #convert_md()
    #
    #render_examples = False
    #
    ## hack for lacking git-lfs support on rtd
    #import git_lfs
    #try:
    #    from urllib.error import HTTPError
    #except ImportError:
    #    from urllib2 import HTTPError
    #
    #_fetch_urls = git_lfs.fetch_urls
    #
    #def _patched_fetch_urls(lfs_url, oid_list):
    #    """Hack git_lfs library that sometimes makes too big requests"""
    #    objects = []
    #
    #    try:
    #        objects.extend(_fetch_urls(lfs_url, oid_list))
    #    except HTTPError as err:
    #        if err.code != 413:
    #            raise
    #        logger.error("LFS: request entity too large, splitting in half")
    #        objects.extend(_patched_fetch_urls(lfs_url, oid_list[:len(oid_list) // 2]))
    #        objects.extend(_patched_fetch_urls(lfs_url, oid_list[len(oid_list) // 2:]))
    #
    #    return objects
    #
    #git_lfs.fetch_urls = _patched_fetch_urls
    #git_lfs.fetch(PROJECT_ROOT_DIR)

    if not os.path.exists('./git-lfs'):
        os.system('wget https://github.com/git-lfs/git-lfs/releases/download/v2.7.1/git-lfs-linux-amd64-v2.7.1.tar.gz')
        os.system('tar xvfz git-lfs-linux-amd64-v2.7.1.tar.gz')
        os.system('./git-lfs install')  # make lfs available in current repository
        os.system('./git-lfs fetch')  # download content from remote
        os.system('./git-lfs checkout')  # make local files to have the real content on them

else:
    render_examples = True


#extensions = ['myst_parser','sphinx_markdown_tables']
extensions = [
    'myst_parser',
    'sphinx_markdown_tables'
    #"sphinxcontrib.mermaid",
    #"sphinx_copybutton",
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

myst_enable_extensions = [
    "tasklist",
    "deflist",
    "dollarmath",
]

templates_path = ['_templates']
exclude_patterns = []
source_encoding = 'utf-8-sig'
language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
#html_static_path = ['_static']
html_extra_path = ['.']  # 确保根目录被包含
html_search_language = 'zh'

print(sys.executable)

