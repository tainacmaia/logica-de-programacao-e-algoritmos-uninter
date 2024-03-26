from IPython.display import clear_output;
loop = True;
while loop == True:
  clear_output();
  print('Bem-vindo(a) à loja da Taina Costa Maia, RU 4631568');
  # Input de valor e quantidade, cálculo do total
  valor = float(input('Entre com o valor unitário do produto (apenas números): '));
  quantidade = int(input('Entre com a quantidade do produto: '));
  desconto = 0
  total_sem_desconto = valor*quantidade;
  # Condicionais de desconto por valor
  if total_sem_desconto < 2500:
    desconto = 0
  elif 2500 <= total_sem_desconto < 6000:
    desconto = 4;
  elif 6000 <= total_sem_desconto < 10000:
    desconto = 7;
  else:
    desconto = 11;
  # Resultado - valores sem e com desconto
  print('O valor sem desconto foi R$ {}' .format(total_sem_desconto));
  total_com_desconto = total_sem_desconto - total_sem_desconto*(desconto/100);
  print('O valor com desconto foi R$ {} (desconto {}%)' .format(total_com_desconto, desconto));
  # Reiniciar programa
  continuar = input('Deseja reiniciar (S/N)? ');
  if continuar == 'N':
    loop = False;