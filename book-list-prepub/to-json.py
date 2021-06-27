import sys
import os
import re
import json


def main():
    parser = RecordParser()
    number_of_lines = parser.parse(sys.stdin)
    print(json.dumps(parser.books_content))


HEADER_STATE = 1
INTRO_STATE = 2
BOOKS_STATE = 3

NO_AUTHOR = '<NO AUTHOR>'
NO_TITLE = '<NO TITLE>'

class RecordParser:
    def __init__(self):
        self.book = None
        self.state = HEADER_STATE
        self.books_content = {
            'header': '',
            'intro': '',
            'books': [],
        }

    def parse(self, in_fp):
        line_number = 0
        for line in in_fp:
            line_number += 1
            self.parseLine(line, line_number)
        if self.book:
            self.books_content['books'].append(self.book)
        return line_number


    def parseLine(self, line, line_number):
        if self.state == BOOKS_STATE:
            self.parseBookLine(line, line_number)
        elif self.state == INTRO_STATE:
            self.parseIntroLine(line, line_number)
        else:
            self.parseHeaderLine(line, line_number)


    def parseBookLine(self, line, line_number):
        line = line.rstrip('\n\r ')
        if not line.lstrip(' '):
            return
        if (is_new_book(line)):
            if self.book:
                self.books_content['books'].append(self.book)
            self.book = new_book_from_line(line, line_number)
        else:
            self.book = add_line(self.book, line, line_number)


    def parseIntroLine(self, line, lineNumber):
        if is_eo_intro(line):
            self.state = BOOKS_STATE
        else:
            self.books_content['intro'] += line


    def parseHeaderLine(self, line, lineNumber):
        if is_so_intro(line):
            self.state = INTRO_STATE
            self.books_content['intro'] = line
        else:
            self.books_content['header'] += line



def is_eo_intro(line):
    return line.startswith('## ')


def is_so_intro(line):
    return line.startswith('## ')


def is_new_book(line):
    return line.startswith('### ')


def new_book():
    return { 'title': NO_TITLE, 'author': NO_AUTHOR, 'remarks': [], 'rating': -1, 'rating_warning': False,
             'sort_keys': {
                 'author': NO_AUTHOR, 'title': NO_TITLE
             }}


def new_book_from_line(title_line, line_number):
    authored_title_line_pattern = re.compile(r'^###\s+(.*)\s+by\s+(.*)$')
    unauthored_title_line_pattern = re.compile(r'^###\s+(.*)$')
    m = authored_title_line_pattern.match(title_line)
    if not m:
        m = unauthored_title_line_pattern.match(title_line)
        if not m:
            raise ValueError('Bad title line: {}, "{}"'.format(line_number, title_line))
    book = new_book()
    book['title'] = m.group(1)
    if len(m.groups()) == 2:
        book['author'] = m.group(2)
    book = set_sort_keys(book)
    return book


def add_line(book, line, line_number):
    if line.startswith('- '):
        add_remark_line(book, line, line_number)
    elif line.startswith('rating: '):
        add_rating_line(book, line, line_number)
    else:
        raise ValueError('Unexpected line: {}, "{}"'.format(line_number, line))
    return book


def add_remark_line(book, line, line_number):
    remark = line.lstrip('- ')
    book['remarks'].append(remark)
    return book


def set_sort_keys(book):
    book['sort_keys']['author'] = extract_author_sort_key(book['author'])
    book['sort_keys']['title'] = extract_title_sort_key(book['title'])
    return book

def extract_author_sort_key(author):
    if author == NO_AUTHOR:
        return author
    words = author.split()
    if words[0] == 'The':  # assume no-one is called 'The'
        return words[0]
    else:
        return words.pop()

def extract_title_sort_key(title):
    return title




def add_rating_line(book, line, line_number):
    rating_pattern = re.compile(r'rating: (\d+)\s*(warning)?')
    m = rating_pattern.match(line)
    if m:
        book['rating'] = int(m.group(1))
        if m.group(2):
            book['rating_warning'] = True
    return book


if __name__ == '__main__':
    main()

