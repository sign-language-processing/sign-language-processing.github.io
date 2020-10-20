markdown: dst dst/index.html dst/style.css

server: dst dst/style.css dst/index.md

dst/index.html: dst/index.md src/references.bib
	pandoc dst/index.md -s --table-of-contents --bibliography=src/references.bib --columns 1000  -o $@

dst/index.pdf: dst/index.md src/references.bib
	cd dst && pandoc index.md -s -N --pdf-engine=xelatex --bibliography=../src/references.bib -o index.pdf


dst/index.md: src/index.md src/formats.md src/gtag.html dst tmp/datasets.md dst/assets
	cat src/index.md > $@
	sed -i -e '/formats.md/{r src/formats.md' -e 'd}' $@
	sed -i -e '/gtag.html/{r src/gtag.html' -e 'd}' $@
	sed -i -e '/datasets.md/{r tmp/datasets.md' -e 'd}' $@
	sed -i 's/TODO/\<span style=\"background-color: red; color: white; padding: 0 2px !important;\"\>TODO\<\/span\>/g' $@

dst/style.css: dst src/styles/splendor.css src/styles/custom.css
	cat src/styles/splendor.css src/styles/custom.css > $@

# TODO make this depend on all asset files
dst/assets: src/assets/tasks.svg
	mkdir -p $@
	cp -r src/assets/* $@

dst:
	mkdir $@


# Temporary files
tmp:
	mkdir $@

# TODO make this depend on all dataset json files
tmp/datasets.md: src/datasets.js tmp
	node src/datasets.js > $@

#
#latex: tex/main.tex
#
#tex:
#	mkdir $@
#
#tex/main.tex: dst/index.md tex/references.bib tex
#	pandoc dst/index.md -s -N --natbib --bibliography=references.bib -o $@
#
#
#
#tex/references.bib: src/references.bib tex
#	cp src/references.bib $@
