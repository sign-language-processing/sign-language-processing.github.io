const fs = require('fs');

function link(title, href) {
    let s = title;

    if (href) {
        s = `<a href="${href}" title="${title}">${s}</a>`;
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
    return `<img alt="${type}"title="${specificity || ""}" class="data-feature" src="assets/icons/${type}.png" />`;
}


const PATH = "src/datasets/";

const datasets = fs.readdirSync(PATH)
    .map(fName => String(fs.readFileSync(PATH + fName)))
    .map(d => JSON.parse(d))
    .sort((a, b) => a.pub.name.toLowerCase() > b.pub.name.toLowerCase() ? 1 : -1);


console.log('<table cellspacing="0" border="1" style="max-width: 100%;">')
console.log(`<thead>
<tr>
<th>Dataset</th>
<th>Publication</th>
<th>Language</th>
<th>Features</th>
<th>#Signs</th>
<th>#Samples</th>
<th>#Signers</th>
<th>License</th>
</tr>
</thead><tbody>`)

for (const dataset of datasets) {
    console.log("<tr>")
    console.log("<td>", link(dataset.pub.name, dataset.pub.url), "</td>");
    console.log("<td>", dataset.pub.publication ? `@${dataset.pub.publication}` : dataset.pub.year || "", "</td>");
    console.log("<td>", dataset.language, "</td>");
    console.log("<td>", dataset["features"].length ? dataset["features"].map(getIcon).join("") : "TODO", "</td>");
    console.log("<td>", dataset["#items"] ? dataset["#items"].toLocaleString('en-US') : "", "</td>");
    console.log("<td>", sanitize(dataset["#samples"]) || "", "</td>");
    console.log("<td>", dataset["#signers"] || "", "</td>");
    console.log("<td>", link(dataset.license, dataset.licenseUrl) || "TODO", "</td>");
    console.log("</tr>")
}

console.log("</tbody></table>")
