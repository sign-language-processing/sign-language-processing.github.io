markdown: dst dst/index.html dst/style.css

server: dst dst/style.css dst/index.md dst/sitemap.xml

dst/index.html: dst/index.md src/references.bib src/template/index.html dst/style.css
	pandoc dst/index.md --template src/template/index.html -s --table-of-contents --bibliography=src/references.bib --citeproc --columns 1000 -H src/header.html -V lang=en -o $@

dst/index_shortcode.md: dst/index.md
	node addons/emoji-to-shortcode/main.js dst/index.md > $@

dst/index.pdf: dst/index_shortcode.md src/references.bib
	cd dst && pandoc -f markdown+emoji -L../addons/latex-emoji.lua index_shortcode.md -s -N --pdf-engine=lualatex --shift-heading-level-by=-1 --bibliography=../src/references.bib --citeproc -o index.pdf

dst/thesis.pdf: dst/index_shortcode.md src/references.bib
	#pandoc -f markdown+emoji -L addons/latex-emoji.lua src/thesis/main.tex -s -N --pdf-engine=lualatex --shift-heading-level-by=-1 --bibliography=src/references.bib --citeproc -o index.pdf
	cd src/thesis && pandoc main.tex -s -N --natbib --pdf-engine=xelatex -o index.pdf


dst/index.md: src/index.md src/markdown_fix.sh src/formats.md dst tmp/datasets.md dst/assets
	cat src/index.md > $@
	bash src/markdown_fix.sh $@

dst/style.css: dst src/styles/custom.css
	cat src/styles/custom.css > $@

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
	cd dst && pandoc -f markdown+emoji -L../addons/latex-emoji.lua index_shortcode.md --shift-heading-level-by=-1 -s -N --natbib -o index.tex

#
#
#tex/references.bib: src/references.bib tex
#	cp src/references.bib $@
