const fs = require('fs');

// If href is provided, format the string as a markdown link
function createMarkdownLink(title, href) {
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

    if (typeof text === 'number') {
        return String(text);
    }
    // Replace '>' with escaped version
    return text.replace(/>/, "\\>");
}

function getIcon(feature) {
    // Split the feature (e.g. "pose:OpenPose") into type and specificity ("pose" and "OpenPose")
    // allows various specific features with the same type (pose:OpenPose and pose:MediaPipe) to get the same icon.
    const [type, specificity] = feature.split(":");

    const featureEmojiDict = {
        'video': '🎥',
        'pose': '👋',
        'mouthing': '👄',
        'writing': '✍',
        'gloss': '📋',
        'text': '📜',
        'speech': '🔊',
    };

    return `<span title="${feature}">${featureEmojiDict[type]}</span>` || "TODO";
    // return `![${type}](assets/icons/${type}.png "${feature}")`;
}

function printRow(row) {
    console.log('|', row.join(' | '), '|');
}

const PATH = "src/datasets/";

const datasets = fs.readdirSync(PATH) // Read all filenames in the directory * 
    .map(fName => String(fs.readFileSync(PATH + fName))) // Read each file's content and convert to string *
    .map(d => JSON.parse(d)) // Parse the JSON content. * 
    .sort((a, b) => a.pub.name.toLowerCase() > b.pub.name.toLowerCase() ? 1 : -1); // Sort datasets by publication name *

const columns = ['Dataset', 'Publication', 'Language', 'Features', '#Signs', '#Samples', '#Signers', 'License'];
const lengths = [4, 7, 3, 2, 2, 5, 2, 5];

printRow(columns);

// divider row
console.log('|' + lengths.map((l) => new Array(l).fill('-').join('')).join(' | ') + '|');

const downloadEmoji = '💾';

for (const dataset of datasets) {

    if (dataset.status === "deprecated") {
        continue;
    }

    let title = createMarkdownLink(dataset.pub.name, dataset.pub.url);

    if (dataset.loader) {
        const sld = 'https://github.com/sign-language-processing/datasets/tree/master/sign_language_datasets/datasets/' + dataset.loader;
        title += ' ' + createMarkdownLink(downloadEmoji, sld);
    }


    // note - falsy (empty, null, etc) values just replaced with blank strings
    const row = [
        title,
        dataset.pub.publication ? `@${dataset.pub.publication}` : dataset.pub.year || "", // add citation syntax @citationkey. Make/Pandoc later replace with citation
        dataset.language,
        dataset["features"].length ? dataset["features"].map(getIcon).join("") : "TODO",
        dataset["#items"] ? dataset["#items"].toLocaleString('en-US') : "",
        sanitize(dataset["#samples"]) || "",
        dataset["#signers"] || "",
        createMarkdownLink(dataset.license, dataset.licenseUrl)
    ];


    printRow(row);
}
