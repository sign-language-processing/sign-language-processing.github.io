const fs = require('fs');

function link(title, href) {
    if (!title) {
        return "";
    }

    let s = title;

    if (href) {
        s = `<a href="${href}" title="${title}">${s}</a>`;
    }

    return s;
}


const PATH = "src/datasets/";

const datasets = fs.readdirSync(PATH)
    .map(fName => String(fs.readFileSync(PATH + fName)))
    .map(d => JSON.parse(d))
    .sort((a, b) => a.pub.name > b.pub.name ? 1 : -1);


console.log('<table cellspacing="0" border="1" style="max-width: 100%;">')
console.log(`<thead>
<tr>
<th>Dataset</th>
<th>Publication</th>
<th>Language</th>
<th>#Items</th>
<th>#Samples</th>
<th>#Signers</th>
<th>Notes</th>
<th>License</th>
</tr>
</thead><tbody>`)

for (const dataset of datasets) {
    console.log("<tr>")
    console.log("<td>", link(dataset.pub.name, dataset.pub.url), "</td>");
    console.log("<td>", dataset.pub.publication ? `@${dataset.pub.publication}` : dataset.pub.year || "", "</td>");
    console.log("<td>", dataset.language, "</td>");
    console.log("<td>", dataset["#items"] || "", "</td>");
    console.log("<td>", dataset["#samples"] || "", "</td>");
    console.log("<td>", dataset["#signers"] || "", "</td>");
    console.log("<td>", dataset["notes"] || "", "</td>");
    console.log("<td>", link(dataset.license, dataset.licenseUrl), "</td>");
    console.log("</tr>")
}

console.log("</tbody></table>")
