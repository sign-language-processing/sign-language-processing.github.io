markdown: dst dst/index.html dst/style.css

server: dst dst/style.css tmp/processed_index.md

dst/index.html: tmp/processed_index.md src/references.bib
	pandoc tmp/processed_index.md -s --table-of-contents --bibliography=src/references.bib --columns 1000  -o $@

tmp/processed_index.md: src/index.md src/formats.md src/gtag.html tmp tmp/datasets.md dst/assets
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
tmp/datasets.md: src/datasets.js
	node src/datasets.js > $@


latex: tex/main.tex

tex:
	mkdir $@

tex/main.tex: tmp/processed_index.md tex/references.bib tex
	pandoc tmp/processed_index.md -s -N --natbib --bibliography=references.bib -o $@

tex/main.pdf: tmp/processed_index.md src/references.bib tex
	# cd tex && C:/Program\ Files/MiKTeX/miktex/bin/x64/pdflatex.exe main.tex > main.pdf
	pandoc tmp/processed_index.md -s -N --pdf-engine='C:\Program Files\MiKTeX\miktex\bin\x64\pdflatex.exe' --bibliography=src/references.bib -o $@


tex/references.bib: src/references.bib tex
	cp src/references.bib $@
