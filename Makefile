dst/index.html: src/index.md src/formats.html dependencies
	pandoc -o dst/index.html -s --bibliography=src/references.bib src/index.md

dependencies: datasets assets dst

datasets: dst
	node src/datasets.js > dst/datasets.html

assets: dst
	cp -r src/assets dst/assets

dst:
	mkdir -p dst
