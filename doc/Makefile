# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SWITCH_BRANCH = echo "Switching to gh-pages branch..."; git checkout gh-pages; git checkout master -- ../doc ../vice
SPHINXOPTS    = -W
SPHINXBUILD   = sphinx-build2
PAPER         =
BUILDDIR      = ..

GITHUB_REPO    = http://aspidites.github.com/ViCE

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) source

.PHONY: help clean html dirhtml singlehtml pickle json htmlhelp qthelp devhelp epub latex latexpdf text man changes linkcheck doctest gettext

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  gh-pages   to make standalone HTML files and push them to github"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  pickle     to make pickle files"
	@echo "  json       to make JSON files"
	@echo "  htmlhelp   to make HTML files and a HTML help project"
	@echo "  qthelp     to make HTML files and a qthelp project"
	@echo "  devhelp    to make HTML files and a Devhelp project"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  man        to make manual pages"
	@echo "  texinfo    to make Texinfo files"
	@echo "  info       to make Texinfo files and run them through makeinfo"
	@echo "  gettext    to make PO message catalogs"
	@echo "  changes    to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck  to check all external links for integrity"
	@echo "  doctest    to run all doctests embedded in the documentation (if enabled)"
	@echo "  coverage   to collect documentation coverage stats"

clean:
	find $(BUILDDIR)/* -maxdepth 0 -name 'vice' -o -name 'doc' -prune -o -exec rm -rf '{}' ';'

html:
	./convert_svgs.sh
	$(SWITCHBRANCH)
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

epub:
	./convert_svgs.sh
	$(SWITCHBRANCH)
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

gh-pages:
	./convert_svgs.sh
	$(SWITCHBRANCH)
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)
	@echo "Build finished. The html pages are in the gh-pages branch's root."
	git add ..
	git commit -am "Updated documentation."
	git push origin gh-pages
	@echo "Documentation published: http://aspidites.github.com/ViCE"
	@echo "Switching back to master branch..."
	git checkout master


latexpdf:
	./convert_svgs.sh
	$(SWITCHBRANCH)
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

linkcheck:
	./convert_svgs.sh
	$(SWITCHBRANCH)
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	./convert_svgs.sh
	$(SWITCHBRANCH)
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

coverage:
	./convert_svgs.sh
	$(SWITCHBRANCH)
	$(SPHINXBUILD) -b coverage $(ALLSPHINXOPTS) $(BUILDDIR)/coverage
	@echo
	@echo "Coverage check finished, results in $(BUIDDIR)/coverage/."
