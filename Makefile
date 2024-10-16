markdown: dst dst/index.html dst/style.css

server: dst dst/style.css dst/index.md dst/sitemap.xml

# CDL: this is where the bibliography @ citations are transformed, I believe, to things like (Someone 2024)
# also, requires a newer version of pandoc, in order to use --citeproc
# https://pandoc.org/releases.html#pandoc-2.11-2020-10-11 or greater,
# which means that on Ubuntu you may need to go directly to the source repo and download/install the .deb
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


dst/sections: dst/index.tex
	python src/split_sections.py


overleaf: dst/sections tmp
	rm -rf tmp/overleaf
	git clone https://git.overleaf.com/611a535f64617c334d122e31 tmp/overleaf
	mkdir -p tmp/overleaf/parts/background
	cp -r dst/sections tmp/overleaf/parts/background
	rm -f tmp/overleaf/parts/background/sections/.DS_Store
	cp -r dst/assets tmp/overleaf/parts/background
	cp src/references.bib tmp/overleaf/parts/background
	rm -f tmp/overleaf/parts/background/assets/.DS_Store
	cd tmp/overleaf && \
		git add -A && \
		git commit -am "autoamtic sections upload" && \
		git push

#
#latex: tex/main.tex
#
#tex:
#	mkdir $@
#
dst/index_emoji.tex: dst dst/index_shortcode.md src/references.bib
	pandoc -f markdown+emoji -L addons/latex-emoji.lua dst/index_shortcode.md --shift-heading-level-by=-1 -s -N --natbib -o $@

dst/index.tex: dst/index_emoji.tex src/replace_gifs.py
	python src/replace_gifs.py dst/index_emoji.tex $@

#
#
#tex/references.bib: src/references.bib tex
#	cp src/references.bib $@
