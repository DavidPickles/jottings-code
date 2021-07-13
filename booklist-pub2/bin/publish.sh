#!/usr/bin/env bash
set -o errexit
set -o nounset

pub_file_path=$(greadlink -f '../../jottings')'/books.yml'
publish_dir=$(greadlink -f '../../jottings-pub')



function publish() {
    if [ ! -s "$pub_file_path" ]; then
        echo "$pub_file_path is empty!"
        exit 1
    fi

    pushd "$publish_dir"
    git checkout main
    popd

    cp "$pub_file_path" "$publish_dir"

    pushd "$publish_dir"
    git add .
    git status
    git commit -m 'new book record'
    git push
    popd
}

publish
