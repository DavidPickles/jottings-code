#!/usr/bin/env bash
set -o errexit
set -o nounset

content=$1
sort=$2
renderer=${3:-'echo'}

if [ "$content" = 'books-only' ]; then
  jq_code="{ books: (.books | sort_by(.sort_keys.$sort))}"
else
  jq_code="del(.books) + { books: (.books | sort_by(.sort_keys.$sort))}"
fi

python3 to-json.py \
  | jq "$jq_code" \
  | python3 to-output.py "$renderer"


