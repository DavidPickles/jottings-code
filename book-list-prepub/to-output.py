import sys
import os
import json
import importlib
import re

LAYOUTS_DIR = 'layouts'

def main():
    if len(sys.argv) != 2:
        raise Exception("Gimme a layout module file path".format(sys.argv[0]))
        sys.exit()

    if sys.argv[1] == 'echo':
        sys.stdout.write(sys.stdin.read())
        sys.exit()

    layout = load_layout(sys.argv[1])

    books_content = json.load(sys.stdin)

    if 'header' in books_content:
        print(books_content['header'], end='')
    if 'intro' in books_content:
        print(books_content['intro'], end='')

    for cnt, book in enumerate(books_content['books']):
        layout.print_book(book)



def load_layout(lomod_filename):
    return importlib.import_module( LAYOUTS_DIR + '.' + lomod_filename )


def main_title_of(book):
    return re.sub(r'^The\s+',  '', book['title'], 1)

if __name__ == '__main__':
    main()

