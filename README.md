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