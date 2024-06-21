# Sign Language Processing

The goal of this project is to contain and organize the sign language processing literature, datasets, and tasks.

This project is hosted in: [sign-language-processing.github.io](https://sign-language-processing.github.io)

Contributions are welcomed!

## Building

The hosted github page is automatically built on push to master.

To build the page locally, run `make`.

Make sure you have [pandoc](https://pandoc.org/) installed.

## Development
To continuously build the page locally, listening to changes, run:
```bash
watch make
```
(or in bash, run `while true; do make; sleep 2; done`)
And view the result by
```bash
npm i -g http-server
http-server dst
```

## Citation

For attribution in academic contexts, please cite this work as:

```bibtex
@misc{moryossef2021slp, 
    title = "{S}ign {L}anguage {P}rocessing", 
    author = "Moryossef, Amit and Goldberg, Yoav",
    howpublished = "\url{https://sign-language-processing.github.io/}",
    year = "2021"
}
```

## Style Guide

- **Citations**: Use the format `@authorYearKeyword` for inline citations, and `[@authorYearKeyword]` for citations wrapped in parentheses. To include multiple citations ,use a semicolon (;) to separate them (e.g., "@authorYearKeyword;@authorYearKeyword").
- **Background & Related Work**: Use simple past tense to describe previous work (e.g., "@authorYearKeyword used...").
- **Abbreviations**: Define abbreviations in parentheses after the full term (e.g., Langue des Signes Française (LSF)).
- **Percentages**: Use the percent sign (%) with no space between the number and the sign (e.g., 95%).
- **Spacing**: Use a single space after periods and commas.
- **Hyphenation**: Use hyphens (-) for compound adjectives (e.g., video-to-pose).
- **Lists**: Use "-" for list items, followed by a space.
- **Code**: Use backticks (`) for inline code, and triple backticks (```) for code blocks.
- **Numbers**: Spell out numbers less than 10, and use numerals for 10 and greater.
- **Contractions**: Avoid contractions (e.g., use "do not" instead of "don't").
- **Compound Words**: Use a forward slash (/) to separate alternative compound words (e.g., 2D / 3D).
- **Phrasing**: Prefer active voice over passive voice (e.g., "The authors used..." instead of "The work was used by the authors...").
- **Structure**: Present information in a logical order.
- **Capitalization**: Capitalize the first word of a sentence, and proper nouns.
- **Emphasis**: Use italics for emphasis by wrapping a word with asterisks (e.g., *emphasis*).
- **Quote marks**: Use double quotes (").
- **Paragraphs**: When a subsection header starts with ######, add "{-}" to the end of the subsection title to indicate a new paragraph. If it starts with #, ##, ###, ####, or ##### do not add the "{-}".
- **Mathematics**: Use LaTeX math notation (e.g., $x^2$) wrapped in dollar signs ($).

Please help me edit the following text to be consistent with the style guide.
Make sure to maintain the original line breaks (i.e., don't merge lines, and conserve \n characters).
Reply with a code block.

```md

```

Respond in a Markdown code block, conserving \n characters.

Respond in a Markdown code block.
Conserve \n characters (new-line characters).
i.e., break line before "They parse the English text..."


### Code Style

Some guidelines for good code and commenting style.

#### Commenting

- Comments should not be redundant. Meaning, that if someone with a basic knowledge of the programming languaged can tell at a glance what it does, there's no need to explain. For example, the JavaScript `const fs = require('fs');` does not need to be explained.
- Don't use personal sign-offs or openings, the code should exist regardless of authors. For example `// maps to emoji`, not `//Colin: maps to emoji`.

#### Further Reading

Google has a [Javascript Style guide](https://google.github.io/styleguide/jsguide.html).
