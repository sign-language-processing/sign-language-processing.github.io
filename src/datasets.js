const fs = require('fs');

function link(title, href) {
    let s = title;

    if (href) {
        s = `[${s}](${href})`;
    }

    return s;
}

function sanitize(text) {
    if (!text) {
        return text;
    }
    return text.replace(/>/, "\\>")
}

function getIcon(feature) {
    const [type, specificity] = feature.split(":");
    const dict = {
        'video': '🎥',
        'pose': '👋',
        'mouthing': '👄',
        'writing': '✍',
        'gloss': '📋',
        'text': '📜',
        'speech': '🔊',
    };
    return `<span title="${feature}">${dict[type]}</span>` || "TODO";
    // return `![${type}](assets/icons/${type}.png "${feature}")`;
}

function printRow(row) {
    console.log('|', row.join(' | '), '|');
}


const PATH = "src/datasets/";

const datasets = fs.readdirSync(PATH)
    .map(fName => String(fs.readFileSync(PATH + fName)))
    .map(d => JSON.parse(d))
    .sort((a, b) => a.pub.name.toLowerCase() > b.pub.name.toLowerCase() ? 1 : -1);


const columns = ['Dataset', 'Publication', 'Language', 'Features', '#Signs', '#Samples', '#Signers', 'License'];
const lengths = [4, 7, 3, 2, 2, 5, 2, 5]
// console.log('<table cellspacing="0" border="1" style="max-width: 100%;">')
printRow(columns); // Header row
console.log('|' + lengths.map((l) => new Array(l).fill('-').join('')).join(' | ') + '|'); // Divider row

const downloadEmoji = '💾';

for (const dataset of datasets) {
    let title = link(dataset.pub.name, dataset.pub.url);
    if (dataset.loader) {
        const sld = 'https://github.com/sign-language-processing/datasets/tree/master/sign_language_datasets/datasets/' + dataset.loader;
        title += ' ' + link(downloadEmoji, sld);
    }

    const row = [
        title,
        dataset.pub.publication ? `@${dataset.pub.publication}` : dataset.pub.year || "",
        dataset.language,
        dataset["features"].length ? dataset["features"].map(getIcon).join("") : "TODO",
        dataset["#items"] ? dataset["#items"].toLocaleString('en-US') : "",
        sanitize(dataset["#samples"]) || "",
        dataset["#signers"] || "",
        link(dataset.license, dataset.licenseUrl)
    ];
    printRow(row);
}
