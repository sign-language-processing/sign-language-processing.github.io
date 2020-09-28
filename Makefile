dst/index.html: src/index.md src/formats.html datasets assets dst
	pandoc -o dst/index.html -s --bibliography=src/references.bib  src/index.md


datasets: dst
	node src/datasets.js > dst/datasets.html

assets: dst
	cp -r src/assets dst/assets

dst:
	mkdir -p dst
