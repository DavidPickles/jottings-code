
def print_book(book):
    print('#### ', end='')
    print_author(book['author'])
    print_title(book['title'])
    print_meeting_date(book['meeting_date'])
    print_rating(book['rating'], book['rating_warning'])
    print_remarks(book['remarks'])
    print()


def print_title(title):
    print(" *{}*".format(title))


def print_author(author):
    print(author, end='')


def print_rating(rating, warning):
    if rating == -1:
        print()
    else:
        warningSymbol = ''
        if warning:
            warningSymbol = ' :warning:'
        print('Rating: {}{}'.format(rating, warningSymbol))

def print_meeting_date(meeting_date):
   print('`{} `'.format(meeting_date), end='')

def print_remarks(remarks):
    for cnt, remark in enumerate(remarks):
        print('- {}'.format(remark))
