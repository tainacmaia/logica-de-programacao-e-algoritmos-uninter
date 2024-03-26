print('Bem-vindo(a) à loja de fotocópias da Taina Costa Maia, RU 4631568');
# Função de seleção de serviço
def escolha_servico():
  while True:
    servico = input('DIG - Digitalização\nICO - Impressão Colorida\nIBO - Impressão Preto e Branco\nFOT - Fotocópia\nDigite o código do serviço desejado:\n').upper();
    dict = {'DIG': 1.1, 'ICO': 1, 'IBO': 0.4, 'FOT': 0.2};
    if servico in dict:
      valor_servico = dict[servico];
      print('O serviço custa R$ %.2f por página.' % valor_servico);
      return valor_servico;
    else:
      print('Código do serviço inválido. Tente novamente.');
      continue;
# Função de seleção de quantidade de páginas
def num_pagina():
  while True:
    try:
      total_paginas = int(input('Digite o número de páginas (máximo 20000): '));
      if total_paginas < 20:
        print('Número de paginas: {}' .format(total_paginas))
        return total_paginas;
      elif 20 <= total_paginas < 200:
        print('Por {} páginas, você obteve 15% de desconto!' .format(total_paginas))
        return total_paginas - total_paginas*0.15;
      elif 200 <= total_paginas < 2000:
        print('Por {} páginas, você obteve 20% de desconto!' .format(total_paginas))
        return total_paginas - total_paginas*0.2;
      elif 2000 <= total_paginas <= 20000:
        print('Por {} páginas, você obteve 25% de desconto!' .format(total_paginas))
        return total_paginas - total_paginas*0.25;
      else:
        print("Número máximo de páginas excedido. Tente novamente.");
    except:
      print("Insira uma quantidade de páginas válida.");
# Função de seleção de serviço extra
def servico_extra():
  while True:
    try:
      opcao = int(input('Deseja adicionar mais algum serviço?\n1 - Encadernação Simples - R$ 15,00\n2 - Encadernação Capa Dura - R$ 40,00\n0 - Não desejo mais nada\n'));
      if opcao not in [1,2,0]:
        print('Digite um código válido.');
      else:
        match opcao:
          case 1:
            return 15;
          case 2:
            return 40;
          case 0:
            return 0;
    except:
      print('Digite um código válido.');
# Chamadas para execução da atividade
servico = escolha_servico()
qtd = num_pagina()
extra = servico_extra()
print('Total (R$): %.2f (servico:  %.2f * páginas:  %.2f  + extras:  %.2f)' % ((servico*qtd+extra), servico, qtd, extra))