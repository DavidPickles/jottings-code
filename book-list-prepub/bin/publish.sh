#!/usr/bin/env bash
set -o errexit
set -o nounset

command="$1"
pub_file='book-club-record.md'
render_args='all author simple-md'
prepub_dir='prepub'
pub_file_path="$prepub_dir/$pub_file"
jottings_dir=$(greadlink -f '../../jottings')
publish_dir="$jottings_dir/docs"


function render() {
    /bin/bash bin/render.sh $render_args > "$pub_file_path"
}

function publish() {
    if [ ! -s "$pub_file_path" ]; then
        echo "$pub_file_path is empty! (Did you forget to checkout the master branch of jottings?)"
        exit 1
    fi

    pushd "$jottings_dir"
    git checkout published
    popd

    cp "$pub_file_path" "$publish_dir"

    pushd "$jottings_dir"
    git add "$publish_dir"
    git status
    git commit -m 'new book record'
    git push
    git checkout master
    popd
}

[[ $command =~ r ]] && render
[[ $command =~ p ]] && publish


