# Função de cadastro de livros
def cadastrar_livro(id):
  print('*'*33);
  print('-'*7 + ' Cadastro de livros ' + '-'*7);
  id_livro = id + 1; 
  while True:
    nome = input('Por favor entre com o nome: ');
    autor = input('Por favor entre com o autor: ');
    editora = input('Por favor entre com o editora: ');

    dict = {'ID': id_livro, 'Nome': nome, 'Autor': autor, 'Editora': editora};
    lista_livros.append(dict);
    print("Livro {} do(a) autor(a) {} e editora {} cadastrado com sucesso sob o código {}" .format(nome, autor, editora, id_livro));

    while True:
      cadastrar_mais = input('Deseja cadastrar mais um livro (S/N)? ').upper();
      if (cadastrar_mais == 'S'):
        id_livro += 1;
        break;
      elif (cadastrar_mais == 'N'):
        break;
      else:
        opcao_invalida();
    if(cadastrar_mais == 'N'):
      return id_livro;
# Função de consulta de livros
def consultar_livro():
  print('*'*33);
  print('-'*7 + ' Consulta de livros ' + '-'*7);
  while True:
    try:
      opcao = int(input('1 - Consultar Todos\n2 - Consultar por ID\n3 - Consultar por Autor\n4 - Retornar ao menu\nDigite o código da opção desejada: '));
      count = 0;
      if opcao == 1:
        print('-'*30);
        for livro in lista_livros:
          print(f"ID: {livro['ID']}\nNome: {livro['Nome']}\nAutor: {livro['Autor']}\nPagamento: {livro['Editora']}");
          print('-'*30);
          count += 1
        if count == 0:
          print("Nenhum livro encontrado.");
          print('-'*30);
      elif opcao == 2:
        while True:
          try:
            id_livro = int(input("Digite o ID do livro (apenas números): "));
            print('-'*30);
            for livro in lista_livros:
              if livro["ID"] == id_livro:
                print(f"ID: {livro['ID']}\nNome: {livro['Nome']}\nAutor: {livro['Autor']}\nEditora: {livro['Editora']}");
                count += 1
            if count == 0:
              print("Livro não encontrado.");
            print('-'*30);
            break;
          except:
            opcao_invalida();
      elif opcao == 3:
        autor = input("Digite o autor desejado: ");
        print('-'*30);
        for livro in lista_livros:
          if livro["Autor"].upper() == autor.upper():
            print(f"ID: {livro['ID']}\nNome: {livro['Nome']}\nAutor: {livro['Autor']}\nEditora: {livro['Editora']}");
            print('-'*30);
            count += 1;
        if count == 0:
          print("Nenhum livro encontrado.");
          print('-'*30);
      elif opcao == 4:
        print('-'*30);
        print('Saindo da consulta...');
        print('-'*30);
        break;
      else:
        opcao_invalida();
        continue;
    except:
      opcao_invalida();
      continue;
# Função de remoção de livros
def remover_livro():
    print('*'*33);
    print('-'*7 + ' Remoção de livros ' + '-'*7);
    while True:
      try:
        count = 0;
        id_livro = int(input("Digite o ID do livro a ser removido: "));
        for livro in lista_livros:
          if livro["ID"] == id_livro:
            lista_livros.remove(livro);
            print('-'*30);
            print("Livro removido com sucesso!");
            print('-'*30);
            count += 1;
            break;
        if(count == 0):
          print('-'*30);
          print("Livro não encontrado.");
          print('-'*30);
        else:
          break;
      except:
        opcao_invalida();
# Função de aviso de opção inválida
def opcao_invalida():
  print('-'*30);
  print('Desculpe, não entendi. Digite uma opção válida!');
  print('-'*30);
print('Bem-vindo(a)! Sou Taina Costa Maia (RU 4631568), sua assistente virtual.');
id_global = 0;
lista_livros = [];
# Seleção da opção desejada
while True:
  print('Confira as opções: \n 1 - Cadastrar livro\n 2 - Consultar livro\n 3 - Remover livro\n 4 - Encerrar programa');
  opcao = int(input('O que você deseja fazer? Digite um número: '));
  if opcao not in [1,2,3,4]:
    opcao_invalida();
    continue;
  else:
    match opcao:
      case 1:
        id_global = cadastrar_livro(id_global);
      case 2:
        consultar_livro();
      case 3:
        remover_livro();
      case 4:
        print('-'*30);
        print('Até logo!');
        break;