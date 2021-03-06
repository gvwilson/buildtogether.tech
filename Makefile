JEKYLL=bundle exec jekyll
SITE=./_site
LANGUAGE=en

CONFIG=_config.yml
INCLUDES=$(wildcard _includes/*)
LAYOUTS=$(wildcard _layouts/*.html)
MARKDOWN=$(wildcard *.md) $(wildcard */index.md)
HTML=${SITE}/index.html $(wildcard ${SITE}/*/index.html)
EXERCISES=$(wildcard */x-*/problem.md) $(wildcard */x-*/solution.md)
STATIC=$(wildcard static/*.*)
TEX=$(wildcard tex/*.*)

BIB_YAML=_data/bibliography.yml
BIB_MD=bibliography/index.md
GLOSSARY_IN=_data/glossary.yml
HOME_PAGE=${SITE}/index.html
NUM_OUT=_data/numbering.yml
TERMS_OUT=_data/terms.yml
ALL_OUT=${BIB_MD} ${NUM_OUT} ${TERMS_OUT}
EXTRA_MARKDOWN=_includes/intro.md

RELEASE_FILES=\
  CONDUCT.md\
  CONTRIBUTING.md\
  Makefile\
  Gemfile\
  Gemfile.lock\
  _includes\
  _layouts\
  bin\
  favicon.ico\
  glossary\
  links\
  static/local.*\
  static/*.pdf\
  static/*.svg\
  tex

RELEASE_EXCLUDES=\
  _includes/intro.md\
  bin/__pycache__\
  bin/__pycache__/*\
  misc\
  misc/*.*\
  *~

.DEFAULT: commands

## commands: show available commands
commands:
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' | column -t -s ':'

## build: rebuild site without running server
build: ${ALL_OUT} LICENSE.md
	${JEKYLL} build

## serve: build site and run server
serve: ${ALL_OUT} LICENSE.md
	${JEKYLL} serve

## book.tex: create LaTeX file
book.tex: ${HOME_PAGE} bin/html2tex.py ${NUM_OUT} ${TEX}
	bin/html2tex.py --config ${CONFIG} --numbering ${NUM_OUT} --site _site --head tex/head.tex --foot tex/foot.tex > book.tex

## book.pdf: create PDF file
book.pdf: book.tex ${TEX}
	@pdflatex book
	@pdflatex book

## make-bib-md: create Markdown version of bibliography
make-bib-md: ${BIB_MD}

## make-numbering: create YAML cross-referencing
make-numbering: ${NUM_OUT}

## make-spelling: create list of unknown words
make-spelling: ${HOME_PAGE}
	@cat ${HTML} | aspell -H list | sort | uniq

## make-terms: create YAML file listing terms per chapter
make-terms: ${TERMS_OUT}

${BIB_MD}: ${BIB_YAML} bin/make-bib-md.py
	bin/make-bib-md.py --input ${BIB_YAML} --output ${BIB_MD}

${NUM_OUT}: bin/make-numbering.py ${CONFIG} ${MARKDOWN}
	 bin/make-numbering.py --config ${CONFIG} --output ${NUM_OUT}

${TERMS_OUT}: bin/make-terms.py ${CONFIG} ${MARKDOWN} ${GLOSSARY_IN}
	bin/make-terms.py --config ${CONFIG} --glossary ${GLOSSARY_IN} --language ${LANGUAGE} --output ${TERMS_OUT}

${HOME_PAGE}: ${CONFIG} ${MARKDOWN} ${INCLUDES} ${LAYOUTS} ${STATIC} ${ALL_OUT} LICENSE.md
	${JEKYLL} build

$(filter-out bin/utils.py,$(wildcard bin/*.py)): bin/utils.py
	touch $@

LICENSE.md: _config.yml bin/make-license.py
	@bin/make-license.py --config ${CONFIG} --output $@

## ----

## check: run all checks
check:
	@make check-bib
	@make check-boilerplate
	@make check-chunk-length
	@make check-code-blocks
	@make check-gloss
	@make check-links
	@make check-numbering
	@make check-spelling

## check-bib: compare citations and definitions
check-bib:
	@bin/check-bib.py --bibliography ${BIB_YAML} --sources ${MARKDOWN} _includes/intro.md

## check-boilerplate: check standard files
check-boilerplate:
	@bin/check-boilerplate.py --config ${CONFIG} --license LICENSE.md

## check-chunk-length: see whether any inclusions are overly long
check-chunk-length:
	@bin/check-chunk-length.py --sources ${HTML}

## check-code-blocks: check inline code blocks
check-code-blocks:
	@bin/check-code-blocks.py --sources ${MARKDOWN}

## check-gloss: compare references and definitions
check-gloss:
	@bin/check-gloss.py --glossary ${GLOSSARY_IN} --language ${LANGUAGE} --sources ${MARKDOWN} ${EXERCISES}

## check-links: make sure all external links resolve
check-links:
	@bin/check-links.py --config ${CONFIG} --sources ${MARKDOWN} ${EXTRA_MARKDOWN} ${EXERCISES}

## check-numbering: make sure all internal cross-references resolve
check-numbering: ${NUM_OUT}
	@bin/check-numbering.py --numbering ${NUM_OUT} --sources ${MARKDOWN} ${EXERCISES}

## check-spelling: check for misspelled words
check-spelling: ${HOME_PAGE}
	@cat ${HTML} | aspell -H list | sort | uniq | bin/check-spelling.py --compare _data/spelling.txt

## ----

## list-html-attributes: what classes and other attributes are used?
list-html-attributes: ${HOME_PAGE}
	@bin/list-html-attributes.py --sources ${HTML}

## release: make a zip file with infrastructure for use elsehwere
release:
	@zip -r ../template.zip ${RELEASE_FILES} --exclude ${RELEASE_EXCLUDES}

## show-pages: how many pages are in the PDF version?
show-pages: book.pdf
	@bin/show-pages.py --input book.aux | column -t -s '|'

## show-sections: how many words are in each section?
show-sections:
	@bin/show-sections.py --config ${CONFIG} | column -t -s '|'

## clean: clean up stray files
clean:
	@find . -name '*~' -exec rm {} \;
	@rm -f *.aux *.log *.out *.tex *.toc

## sterile: clean up and erase generated site
sterile:
	@make clean
	@rm -rf ${SITE}

# Local commands if available.
-include local.mk
