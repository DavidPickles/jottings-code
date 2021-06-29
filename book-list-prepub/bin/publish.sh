#!/usr/bin/env bash
set -o errexit
set -o nounset

command="$1"
pub_file='book-club-record.md'
render_args='all author simple-md'
prepub_dir='prepub'
pub_file_path="$prepub_dir/$pub_file"
jottings_dir=$(greadlink -f '../../jottings')
publish_dir=$(greadlink -f '../../jottings-pub')


function render() {
    /bin/bash bin/render.sh $render_args > "$pub_file_path"
}

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

[[ $command =~ r ]] && render
[[ $command =~ p ]] && publish


