dst/index.html: src/index.md src/formats.html datasets assets
	multimarkdown src/index.md > dst/index.html

datasets:
	node src/datasets.js > dst/datasets.html

assets:
	cp -r src/assets dst/assets
