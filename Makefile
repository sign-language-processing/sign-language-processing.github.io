dst/index.html: processed_index src/references.bib
	pandoc -o dst/index.html -s --bibliography=src/references.bib src/processed_index.md

processed_index: src/index.md src/formats.html dependencies
	cat src/index.md > src/processed_index.md
	sed -i -e '/formats.html/{r src/formats.html' -e 'd}' src/processed_index.md
	sed -i -e '/datasets.html/{r dst/datasets.html' -e 'd}' src/processed_index.md

dependencies: datasets assets dst style

datasets: dst
	node src/datasets.js > dst/datasets.html

assets: dst
	mkdir -p dst/assets
	cp -r src/assets/* dst/assets/

style: dst src/styles/splendor.css src/styles/custom.css
	cat src/styles/splendor.css src/styles/custom.css > dst/style.css

dst:
	mkdir -p dst

