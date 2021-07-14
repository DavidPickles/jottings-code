#!/usr/bin/env bash
set -o errexit
set -o nounset

command=$1
pub_file_path=$(greadlink -f '../../jottings')'/books.yml'
publish_proj_dir=$(greadlink -f '../../jottings-pub')
publish_dir="$publish_proj_dir/_data"


function copy() {
  cp -v "$pub_file_path" "$publish_dir"
}

function publish() {
    if [ ! -s "$pub_file_path" ]; then
        echo "$pub_file_path is empty!"
        exit 1
    fi

    pushd "$publish_proj_dir"
    git checkout main
    popd

    copy

    pushd "$publish_proj_dir"
    git add .
    git status
    git commit -m 'new book record'
    git push
    popd
}

[[ $command = c ]] && copy
[[ $command = p ]] && publish
