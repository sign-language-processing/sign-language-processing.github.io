const fs = require('fs')

let content = String(fs.readFileSync(process.argv[process.argv.length - 1]));
const emojis = JSON.parse(String(fs.readFileSync(__dirname + "/emojis.json")))["emojis"];
for (const {emoji, shortname} of emojis) {
    if (content.includes(emoji) && shortname.length > 0) {
        content = content.replace(new RegExp(emoji, 'g'), shortname);
    }
}

console.log(content)
