file = open('input_files/e_so_many_books.txt', 'r')

line = file.readline()

num_books, num_libs, num_days = list(map(int, line.split()))

del line

books_points = file.readline().split()
books_points = list(map(int, books_points))  # index i has book i with its amount of points

print("h")

libraries = []
scanned_books = []

out = ''
days_passed = 0
##################################################################

'''
class Book:
    def __init__(self, score):
        self.score = score
'''

class Library:
    def __init__(self, books, time, num_books, ship_per_day, lib_num):
        self.lib_num = lib_num
        self.books = books
        self.time = time
        self.num_books = num_books
        self.ship_per_day = ship_per_day
        self.scanned = 0
        self.points = 0
        for x in self.books:
            self.points += books_points[x]
        self.score = self.num_books/self.time

    def __str__(self):
        return str(self.lib_num)

    def signup(self, days_passed):
        days_passed += self.time

    def scan_books(self, num_days, days_passed):
        lib_out = ''
        books_scannable = (num_days - days_passed) * self.ship_per_day
        for i in self.books:
            if books_scannable <= 0:
                continue
            if i not in scanned_books:
                scanned_books.append(i)
                lib_out += str(i) + ' '
                books_scannable -= 1
                self.scanned += 1
        return lib_out


c = 0
for i in range(num_libs):
    line = list(map(int, file.readline().split()))  # num of books, signup length, ship per day
    books = list(map(int, file.readline().split())) # index i has book x
    libraries.append(Library(books, line[1], line[0], line[2], c))
    c += 1









libraries.sort(key=lambda x: (-x.score, x.time, -x.ship_per_day))

output = open('hash_answers.txt', 'w')

d = 0
c = 0
out = ''
while days_passed < num_days and d < num_libs:
    libraries[d].signup(days_passed)
    books = libraries[d].scan_books(num_days, days_passed)
    lib_and_books = str(libraries[d].lib_num) + ' ' + str(libraries[d].scanned)
    if libraries[d].scanned > 0:
        out += lib_and_books + '\n' + books + '\n'
        c += 1
    else:
        days_passed -= libraries[d].time
    d += 1



output.write(str(c) + '\n')
output.write(out)

del out







file.close()
output.close()
