const fs = require('fs');

const PATH = "src/datasets/";

const datasets = fs.readdirSync(PATH)
    .map(fName => String(fs.readFileSync(PATH + fName)))
    .map(d => JSON.parse(d))
    .sort((a, b) => a.pub.name > b.pub.name ? 1 : -1);

console.log("```")
console.log(datasets.map(d => JSON.stringify(d)).join("\n"))
console.log("```")

//
// import json
//     from
//
// os
// import listdir,
//
// path
//
// DATASETS_PATH = "src/datasets"
//
// datasets = []
// for file in listdir(DATASETS_PATH):
// f = open(path.join(DATASETS_PATH, file), "r")
// datasets.append(json.load(f))
// f.close()
//
// datasets = sorted(datasets, key = lambda
// d: d["pub"]["year"], reversed = True
// )
//
// print('```')
// print(datasets)
// print('```')
