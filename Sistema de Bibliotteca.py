class Livro:
    def __init__(self, titulo, autor, isbn, preco, editora, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.preco = preco
        self.editora = editora
        self.quantidade = quantidade

class Livraria:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        preco = float(input("Digite o preço do livro: "))
        editora = input("Digite a editora do livro: ")
        quantidade = int(input("Digite a quantidade em estoque: "))
        livro = Livro(titulo, autor, isbn, preco, editora, quantidade)
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Não há livros cadastrados.")
            return
        print("Lista de Livros:")
        for i, livro in enumerate(self.livros):
            print(f"{i+1}. {livro.titulo} - {livro.autor} (ISBN: {livro.isbn})")

    def pesquisar_livro(self):
        busca = input("Digite o título, autor ou ISBN do livro: ")
        livros_encontrados = []
        for livro in self.livros:
            if busca.lower() in livro.titulo.lower() or \
               busca.lower() in livro.autor.lower() or \
               busca.lower() == livro.isbn.lower():
                livros_encontrados.append(livro)
        if livros_encontrados:
            print("Livros encontrados:")
            for i, livro in enumerate(livros_encontrados):
                print(f"{i+1}. {livro.titulo} - {livro.autor} (ISBN: {livro.isbn})")
        else:
            print("Nenhum livro encontrado com essa busca.")

    def alterar_livro(self):
        self.listar_livros()
        if not self.livros:
            return
        indice = int(input("Digite o número do livro que deseja alterar: ")) - 1
        if 0 <= indice < len(self.livros):
            livro = self.livros[indice]
            print("Dados atuais do livro:")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"ISBN: {livro.isbn}")
            print(f"Preço: {livro.preco}")
            print(f"Editora: {livro.editora}")
            print(f"Quantidade: {livro.quantidade}")
            novo_titulo = input("Digite o novo título (ou pressione Enter para manter o atual): ")
            if novo_titulo:
                livro.titulo = novo_titulo
            novo_autor = input("Digite o novo autor (ou pressione Enter para manter o atual): ")
            if novo_autor:
                livro.autor = novo_autor
            novo_isbn = input("Digite o novo ISBN (ou pressione Enter para manter o atual): ")
            if novo_isbn:
                livro.isbn = novo_isbn
            novo_preco = input("Digite o novo preço (ou pressione Enter para manter o atual): ")
            if novo_preco:
                livro.preco = float(novo_preco)
            nova_editora = input("Digite a nova editora (ou pressione Enter para manter a atual): ")
            if nova_editora:
                livro.editora = nova_editora
            nova_quantidade = input("Digite a nova quantidade (ou pressione Enter para manter a atual): ")
            if nova_quantidade:
                livro.quantidade = int(nova_quantidade)
            print("Livro alterado com sucesso!")
        else:
            print("Número de livro inválido.")

    def remover_livro(self):
        self.listar_livros()
        if not self.livros:
            return
        indice = int(input("Digite o número do livro que deseja remover: ")) - 1
        if 0 <= indice < len(self.livros):
            del self.livros[indice]
            print("Livro removido com sucesso!")
        else:
            print("Número de livro inválido.")

# Criar um objeto Livraria
livraria = Livraria()

# Menu interativo
while True:
    print("\nMenu:")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Pesquisar Livro")
    print("4. Alterar Livro")
    print("5. Remover Livro")
    print("6. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        livraria.cadastrar_livro()
    elif opcao == '2':
        livraria.listar_livros()
    elif opcao == '3':
        livraria.pesquisar_livro()
    elif opcao == '4':
        livraria.alterar_livro()
    elif opcao == '5':
        livraria.remover_livro()
    elif opcao == '6':
        break
    else:
        print("Opção inválida!")