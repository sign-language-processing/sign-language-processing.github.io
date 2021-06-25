markdown: dst dst/index.html dst/style.css

server: dst dst/style.css dst/index.md dst/sitemap.xml

dst/index.html: dst/index.md src/references.bib
	pandoc dst/index.md -s --table-of-contents --bibliography=src/references.bib --columns 1000  -o $@ -H src/header.html -V lang=en

dst/index_shortcode.md: dst/index.md
	node addons/emoji-to-shortcode/main.js dst/index.md > $@

dst/index.pdf: dst/index_shortcode.md src/references.bib
	cd dst && pandoc -f markdown+emoji -L../addons/latex-emoji.lua index_shortcode.md -s -N --pdf-engine=lualatex --shift-heading-level-by=-1 --bibliography=../src/references.bib -o index.pdf


dst/index.md: src/index.md src/formats.md dst tmp/datasets.md dst/assets
	cat src/index.md > $@
	sed -i -e '/formats.md/{r src/formats.md' -e 'd}' $@
	sed -i -e '/datasets.md/{r tmp/datasets.md' -e 'd}' $@
	sed -i 's/TODO/\<span style=\"background-color: red; color: white; padding: 0 2px !important;\"\>\*\*TODO\*\*\<\/span\>/g' $@

dst/style.css: dst src/styles/splendor.css src/styles/custom.css
	cat src/styles/splendor.css src/styles/custom.css > $@

dst/sitemap.xml: dst src/sitemap.js
	node src/sitemap.js > $@

# TODO make this depend on all asset files
dst/assets: src/assets/tasks/tasks.svg
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
dst/index.tex: dst dst/index.md src/references.bib
	pandoc dst/index.md -s -N --natbib --bibliography=src/references.bib -o $@

#
#
#tex/references.bib: src/references.bib tex
#	cp src/references.bib $@
