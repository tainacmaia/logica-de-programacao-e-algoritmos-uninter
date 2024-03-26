total = 0;
print('Bem-vindo(a) à açaiteria da Taina Costa Maia, RU 4631568');
# Tabela de preços
print('-'*14 + ' Cardápio ' + '-'*14);
print('| Tamanho | Cupuaçu (CP) | Açaí (AC) |');
print('|    P    |   R$ 10,00   |  R$ 12,00 |');
print('|    M    |   R$ 15,00   |  R$ 17,00 |');
print('|    G    |   R$ 19,00   |  R$ 21,00 |');
print('-'*38);
while True:
  # Escolha do sabor
  while True:
    sabor = input('Digite o código do sabor desejado (AC/CP): ').upper();
    if(sabor == 'AC' or sabor == 'CP'):
      break;
    else:
      print('Sabor inválido. Tente novamente.');
      continue;
  # Escolha do tamanho
  while True:
    tamanho = input('Digite o código do tamanho desejado (P/M/G): ').upper();
    if(tamanho == 'P' or tamanho == 'M' or tamanho == 'G'):
      break;
    else:
      print('Tamanho inválido. Tente novamente.');
      continue;
  # Condicionais da(s) opçõe(s) escolhida(s)
  if(sabor == 'CP' and tamanho == 'P'):
    print('Você pediu um Cupuaçu no valor de R$ 10,00');
    total += 10.00;
  elif(sabor == 'CP' and tamanho == 'M'):
    print('Você pediu um Cupuaçu no valor de R$ 15,00');
    total += 15.00;
  elif(sabor == 'CP' and tamanho == 'G'):
    print('Você pediu um Cupuaçu no valor de R$ 19,00');
    total += 19.00;
  elif(sabor == 'AC' and tamanho == 'P'):
    print('Você pediu um Açaí no valor de R$ 12,00');
    total += 12.00
  elif(sabor == 'AC' and tamanho == 'M'):
    print('Você pediu um Açaí no valor de R$ 17,00');
    total += 17.00
  elif(sabor == 'AC' and tamanho == 'G'):
    print('Você pediu um Açaí no valor de R$ 21,00');
    total += 21.00
  # Determinando encerramento do programa e total a ser pago ou retorno à seleção
  while True:
      pedir_mais = input('Deseja pedir mais alguma coisa (S/N)?').upper();
      if(pedir_mais == 'S'):
        break;
      elif(pedir_mais == 'N'):
        print('O total a ser pago é R$ %.2f' % total);
        break;
      else:
        print('Código inválido. Digite S ou N.');
        continue;
  if(pedir_mais == 'S'):
    continue;
  else:
    break;