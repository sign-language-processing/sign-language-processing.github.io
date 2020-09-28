dst/index.html: src/index.md src/formats.html datasets assets dst
	multimarkdown src/index.md > dst/index.html

datasets: dst
	node src/datasets.js > dst/datasets.html

assets: dst
	cp -r src/assets dst/assets

dst:
	mkdir -p dst
