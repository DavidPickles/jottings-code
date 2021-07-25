This is based on the  booklist source of truth being held in ../jottings/books.yml

The publishing pipeline is:

1. Staging server:  in ../jottings-pub `bundle exec jekyll serve` runs local Jekyll
1. Publish to staging: `bin/publish.sh c` copies books.yml to ../jottings-pub where it is picked up local Jekyll
1. `bin/publish.sh p` publshes to GitHub pages from ../jottings-pub (so run bin/publish.sh c first)

