# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
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
	@echo "  clean      to clean the working tree for a fresh build"
	@echo "  gh-pages   to make standalone HTML files and push them to github"
	@echo "  html       to make standalone HTML files"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  pdf        to make a pdf file directly from source"
	@echo "  coverage   to collect documentation coverage stats"

clean:
	@echo "Switching to gh-pages branch..."
	git checkout gh-pages
	find $(BUILDDIR)/* -maxdepth 0 -name 'vice' -o -name 'doc' -prune -o -exec rm -rf '{}' ';'
	git add ..
	git commit -am "cleaning tree for fresh upload."
	git checkout master
	echo "Clean finished. Please run 'make gh-pages'"

html:
	@echo "Switching to gh-pages branch..."
	git checkout gh-pages
	git checkout master -- ../doc ../vice
	./convert_svgs.sh
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

gh-pages:
	@echo "Switching to gh-pages branch..."
	git checkout gh-pages
	git checkout master -- ../doc ../vice
	./convert_svgs.sh
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)
	@echo "Build finished. The html pages are in the gh-pages branch's root."
	git add ..
	git commit -am "Updated documentation."
	git push origin gh-pages
	@echo "Documentation published: http://aspidites.github.com/ViCE"
	@echo "Switching back to master branch..."
	git checkout master


latexpdf:
	@echo "Switching to gh-pages branch..."
	git checkout gh-pages
	git checkout master -- ../doc ../vice
	./convert_svgs.sh
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	$(MAKE) -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

pdf:
	@echo "Switching to gh-pages branch..."
	./convert_svgs.sh
	$(SPHINXBUILD -b pdf $(ALLSPHINXOPTS) $(BUILDDIR)/pdf
	@echo "Build finished. The PDF files are in $(BUILDDIR)/pdf."

coverage:
	@echo "Switching to gh-pages branch..."
	git checkout gh-pages
	git checkout master -- ../doc ../vice
	./convert_svgs.sh
	$(SPHINXBUILD) -b coverage $(ALLSPHINXOPTS) $(BUILDDIR)/coverage
	@echo
	@echo "Coverage check finished, results in $(BUIDDIR)/coverage/."
