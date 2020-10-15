main: dst dst/index.html dst/style.css

server: dst dst/style.css tmp/processed_index.md

dst/index.html: tmp/processed_index.md src/references.bib
	pandoc -o dst/index.html -s --table-of-contents --bibliography=src/references.bib tmp/processed_index.md

tmp/processed_index.md: src/index.md src/formats.html tmp tmp/datasets.html dst/assets
	cat src/index.md > $@
	sed -i -e '/formats.html/{r src/formats.html' -e 'd}' $@
	sed -i -e '/gtag.html/{r src/gtag.html' -e 'd}' $@
	sed -i -e '/datasets.html/{r tmp/datasets.html' -e 'd}' $@
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
tmp/datasets.html: src/datasets.js
	node src/datasets.js > $@

