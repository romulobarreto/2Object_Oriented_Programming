'''
📌 Cenário:

Vamos modelar um sistema para gerenciar uma biblioteca. Os principais elementos do sistema serão:
	•	Livro (Book): Representa um livro com título, autor e disponibilidade.
	•	Usuário (User): Representa um usuário da biblioteca que pode pegar livros emprestados.
	•	Biblioteca (Library): Gerencia a coleção de livros e os empréstimos.

📝 Planejamento (Passo a Passo):
	1.	Criar a classe Book com atributos básicos e um método para verificar se está disponível.
	2.	Criar a classe User, que pode pegar livros emprestados e devolvê-los.
	3.	Criar a classe Library, que gerencia os livros e controla os empréstimos.
	4.	Implementar um sistema simples de empréstimos.
	5.	Testar o código criando alguns livros e usuários.
'''

# 🖥️ Código Completo
# Filename: object_oriented_modeling.py

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # By default, a book is available

    def __str__(self):
        status = "Available" if self.is_available else "Checked out"
        return f"📖 {self.title} by {self.author} - {status}"


class User:
    """Represents a library user who can borrow books."""

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List of books borrowed

    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            print(f"✅ {self.name} borrowed '{book.title}'")
        else:
            print(f"❌ '{book.title}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"🔄 {self.name} returned '{book.title}'")
        else:
            print(f"⚠️ {self.name} does not have '{book.title}' borrowed.")

    def __str__(self):
        books = ", ".join(book.title for book in self.borrowed_books) if self.borrowed_books else "No books borrowed"
        return f"👤 {self.name} - Borrowed: {books}"


class Library:
    """Represents a library that manages books and loans."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"📚 Added book: '{book.title}' by {book.author}")

    def show_available_books(self):
        print("\n📌 Available Books:")
        available_books = [book for book in self.books if book.is_available]
        if available_books:
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books available.")

    def __str__(self):
        return f"🏛️ Library with {len(self.books)} books."


# ==== TESTING THE SYSTEM ====
if __name__ == "__main__":
    # Creating books
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("The Catcher in the Rye", "J.D. Salinger")

    # Creating a library and adding books
    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Creating a user
    user1 = User("Alice")

    # Display available books
    library.show_available_books()

    # Borrowing books
    user1.borrow_book(book1)
    user1.borrow_book(book2)

    # Showing user's borrowed books
    print(user1)

    # Returning a book
    user1.return_book(book1)

    # Display available books after returning
    library.show_available_books()

'''
🔍 Explicação dos Conceitos Utilizados

1️⃣ Modelagem dos Objetos
	•	Criamos classes para representar os elementos do sistema: Livro (Book), Usuário (User) e Biblioteca (Library).
	•	Cada classe tem seus atributos e métodos bem definidos.

2️⃣ Métodos Especiais
	•	__init__: Construtor para inicializar os atributos.
	•	__str__: Método para representar objetos como string.

3️⃣ Encapsulamento
	•	Os atributos is_available dos livros não podem ser modificados diretamente fora da classe, apenas através de métodos apropriados.

4️⃣ Interação entre Objetos
	•	O User pode pegar emprestado (borrow_book) e devolver (return_book) livros.
	•	A Library gerencia os livros e exibe os disponíveis.

5️⃣ Execução do Código
	•	No final do código, temos um bloco de testes que cria objetos, adiciona livros à biblioteca, permite que um usuário pegue livros emprestados e depois os devolva.
'''