
def print_book(book):
    print('#### ', end='')
    print_author(book['author'])
    print_title(book['title'])
    print_rating(book['rating'], book['rating_warning'])
    print_remarks(book['remarks'])


def print_title(title):
    print(" *{}*".format(title))


def print_author(author):
    print(author, end='')


def print_rating(rating, warning):
    if rating != -1:
        warningSymbol = ''
        if warning:
            warningSymbol = ' :warning:'
        print('rating: {}{}'.format(rating, warningSymbol))


def print_remarks(remarks):
    for cnt, remark in enumerate(remarks):
        print('- {}'.format(remark))
