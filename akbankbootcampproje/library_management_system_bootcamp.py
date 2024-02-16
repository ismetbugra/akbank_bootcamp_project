class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()
    #kitapları listeleyen fonksiyon
    def list_books(self):
        self.file.seek(0)
        #her bir satır bir kitaba denk gelicek
        books = self.file.readlines()
        for book in books:
            #virgülle ayrılmış her kelime kitapla ilgili bir bilgidir
            book_info = book.strip().split(',')
            print(f"Title: {book_info[0]}, Author: {book_info[1]}, Release Year: {book_info[2]}, Number of Pages: {book_info[3]}")

    #dosyaya kitap ekleme işlemi
    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        release_year = input("Enter the release year: ")
        num_pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        #silinecek kitabın titleı bu satırda yoksa bu satırı güncellenmiş kitap listesine eklerr
        for book in books:
            if title not in book:
                updated_books.append(book)
        #eğer girilen title bulunuyorsa updated_books listesine eklenmez böylece tekrar yazıldıgında silinmiş olacak
        #güncellenmiş kitap listesiyle dosyanın içeriğini değiştirir
        self.file.seek(0)
        self.file.truncate()
        #silinmek istenen kitap dışındaki tüm kitaplar dosyaya geri yazılır
        for book in updated_books:
            self.file.write(book)
        print("Book removed successfully.")


lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")
    #kullanıcıdan input alma
    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        #kullanıcı seçimi geçersizse
        print("Invalid choice. Please enter a number between 1 and 4.")