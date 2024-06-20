// CDL: added comments via discussion with ChatGPT 4o: https://chatgpt.com/share/3acd13d8-ddf8-4b71-95af-b7904f806b39
// then manually spot-checked the ones I wasn't sure about.
// "*" means relevant docs at the end 


// Import the NodeJS "file system" module *
const fs = require('fs');

// Function to create a markdown link
function createMarkdownLink(title, href) {
    let s = title; // Initialize link text with title

    // If href is provided, format the string as a markdown link
    if (href) {
        s = `[${s}](${href})`;
    }

    return s; // Return the formatted link or title
}

// Function to sanitize text *
function sanitize(text) {
    // CDL: return unchanged if falsy. Later, falsy values are replaced with ""
    if (!text) {
        return text;
    }
    // If text is a number, convert it to a string 
    if (typeof text === 'number') {
        return String(text);
    }
    // Replace '>' with escaped version
    return text.replace(/>/, "\\>");
}

// Function to get an icon for a feature
function getIcon(feature) {
    // Split the feature into type and specificity
    // CDL: this means that things like pose:OpenPose and pose:MediaPipe get the same icon.
    const [type, specificity] = feature.split(":");
    
    // Dictionary mapping feature types to emoji
    const dict = {
        'video': '🎥',
        'pose': '👋',
        'mouthing': '👄',
        'writing': '✍',
        'gloss': '📋',
        'text': '📜',
        'speech': '🔊',
    };
    
    // Return an HTML span element with the appropriate emoji
    return `<span title="${feature}">${dict[type]}</span>` || "TODO";
    // Alternative return statement for using image icons
    // return `![${type}](assets/icons/${type}.png "${feature}")`;
}

// Function to print a table row
function printRow(row) {
    console.log('|', row.join(' | '), '|'); // Join row elements with ' | ' and print
}

// Define the path to the datasets directory
const PATH = "src/datasets/";

// Read the datasets directory and process each file *
// Colin: => means "Arrow function"* 
const datasets = fs.readdirSync(PATH) // Read all filenames in the directory * 
    .map(fName => String(fs.readFileSync(PATH + fName))) // Read each file's content and convert to string *
    .map(d => JSON.parse(d)) // Parse the JSON content. * 
    .sort((a, b) => a.pub.name.toLowerCase() > b.pub.name.toLowerCase() ? 1 : -1); // Sort datasets by publication name *

// Define column headers and their lengths for the table
const columns = ['Dataset', 'Publication', 'Language', 'Features', '#Signs', '#Samples', '#Signers', 'License'];
const lengths = [4, 7, 3, 2, 2, 5, 2, 5];

// Print the header row
printRow(columns); // Header row
// Print the divider row with dashes
console.log('|' + lengths.map((l) => new Array(l).fill('-').join('')).join(' | ') + '|');

// Define an emoji for download link
const downloadEmoji = '💾';

// Iterate over each dataset to print its details
for (const dataset of datasets) {
    // CDL: should we even include it?
    if(dataset.status === "deprecated"){
        continue; //skip to the next one
    }

    // Create the title link for the dataset
    let title = createMarkdownLink(dataset.pub.name, dataset.pub.url);
    
    // If the dataset has a loader, add a download link
    if (dataset.loader) {
        const sld = 'https://github.com/sign-language-processing/datasets/tree/master/sign_language_datasets/datasets/' + dataset.loader;
        title += ' ' + createMarkdownLink(downloadEmoji, sld);
    }


    // Create a row with the dataset details
    // CDL: falsy (empty, null, etc) values just replaced with blank strings
    const row = [
        title,
        dataset.pub.publication ? `@${dataset.pub.publication}` : dataset.pub.year || "", // add citation syntax. Make/Pandoc later replace with citation
        dataset.language,
        dataset["features"].length ? dataset["features"].map(getIcon).join("") : "TODO",
        dataset["#items"] ? dataset["#items"].toLocaleString('en-US') : "", // if there is an items field, format to standard
        sanitize(dataset["#samples"]) || "",
        dataset["#signers"] || "",
        createMarkdownLink(dataset.license, dataset.licenseUrl)
    ];
    
    // Print the dataset row
    printRow(row);
}

// JavaScript notes for non-JS programmers

// Require: similar to "include" or "import"
// https://www.freecodecamp.org/news/requiring-modules-in-node-js-everything-you-need-to-know-e7fbd119be8/

// Falsy: Includes text with null value, empty strings, etc.
//      https://www.freecodecamp.org/news/falsy-values-in-javascript/
//      https://developer.mozilla.org/en-US/docs/Glossary/Falsy

// File system methods
// https://www.geeksforgeeks.org/node-js-fs-readdirsync-method/
// https://www.geeksforgeeks.org/node-js-fs-readfilesync-method/

// Locale String: helps you reformat to a standard format.
//      e.g. 1234 -> 1,234
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toLocaleString


// Sorting an array of strings
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort

// JSON
// apparently in JavaScript, support for JavaScript Object Notations is built-in. Neat!
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse

// JS ternary operator ?
// Basically an if/else statement. 
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator

// Arrow functions =>
// kinda like a lambda function. For when you want to make a function but NOT name it/keep it around for later
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions

// map: 
//      Used above to run the same (anonymous) function on everything in the array
//      "The map() method of Array instances creates a new array populated with the results of calling a provided function on every element in the calling array."
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map