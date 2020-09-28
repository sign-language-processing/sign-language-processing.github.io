dst/index.html: src/index.md src/formats.html datasets assets
	multimarkdown src/index.md > dst/index.html

datasets: src/datasets/**/*
	node src/datasets.js > dst/datasets.html

assets: src/assets/**/*
	cp -r src/assets dst/assets
