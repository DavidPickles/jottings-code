count = 0

def print_book(book):
    global count
    count += 1
    print(f"({count}) {book['author']} '{book['title']}'")
