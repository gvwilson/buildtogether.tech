include lib/mccole/mccole.mk

## release: make a release
.PHONY: release
ifeq ($(origin BTT_RELEASE),undefined)
release:
	@echo "BTT_RELEASE not defined"
else
release:
	rm -rf docs ${BTT_RELEASE}
	make build
	cp -r docs ${BTT_RELEASE}
	find ${BTT_RELEASE} \( -name .DS_Store -or -name '*.pdf' -or -name '*.aux' -or -name '*.bbl' -or -name '*.bcf' -or -name '*.bib' -or -name '*.blg' -or -name '*.cls' -or -name '*.idx' -or -name '*.ilg' -or -name '*.ind' -or -name '*.log' -or -name '*.tex' -or -name '*.toc' \) -exec rm {} +
endif
