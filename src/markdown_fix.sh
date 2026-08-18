#!/bin/bash

if which gsed >/dev/null
then
  echo "Using gsed"
  function ssed { gsed "$@" ;}
else
  echo "Using sed"
  function ssed { sed "$@" ;}
fi

echo "Fixing $1"

ssed -i -e '/formats.md/{r src/formats.md' -e 'd}' $1
ssed -i -e '/datasets.md/{r tmp/datasets.md' -e 'd}' $1
ssed -i 's/TODO/\<span style=\"background-color: red; color: white; padding: 0 2px !important;\"\>\*\*TODO\*\*\<\/span\>/g' $1
