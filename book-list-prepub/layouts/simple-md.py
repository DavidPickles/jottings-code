
def print_book(book):
    print_title(book['title'])
    print_author(book['author'])
    print_rating(book['rating'], book['rating_warning'])
    print_remarks(book['remarks'])


def print_title(title):
    print('### {}'.format(title), end='')


def print_author(author):
    print(' by {}'.format(author))


def print_rating(rating, warning):
    if rating != -1:
        warningSymbol = ''
        if warning:
            warningSymbol = ' :warning:'
        print('rating: {}{}'.format(rating, warningSymbol))


def print_remarks(remarks):
    for cnt, remark in enumerate(remarks):
        print('- {}'.format(remark))
