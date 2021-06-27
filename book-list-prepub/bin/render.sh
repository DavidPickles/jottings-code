#!/usr/bin/env bash
set -o errexit
set -o nounset

infile=$1
content=$2
sort=$3
renderer=${4:-'echo'}

if [ "$content" = 'books-only' ]; then
  jq_code="{ books: (.books | sort_by(.sort_keys.$sort))}"
else
  jq_code="del(.books) + { books: (.books | sort_by(.sort_keys.$sort))}"
fi

python3 to-json.py < "$infile" \
  | jq "$jq_code" \
  | python3 to-output.py "$renderer"


