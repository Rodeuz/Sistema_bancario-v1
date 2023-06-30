menu = """
[d] para Depositar 
[s] para Sacar 
[e] para ver o Extrato
[n] para Sair

=> """

saldo = 0
limite = 500
extrato = ''
saque_limite = 3
sistema = True

while sistema == True: 
  print(f"\nSaldo Atual: R${format(saldo,'.2f')}\n")
  opcao = input(menu)

  if opcao == "d":
    # extrato
    deposito = float(input("digite quanto deseja depositar: "))

    if deposito < 0:
      print("\n\n valor invalido")
      retorno = input("voltar para o menu ? [s][n]")
      sistema = True if retorno == 's' else False
    else:
      saldo+= deposito
      extrato += (f"Deposito de: R${format(deposito,'.2f')} \n") 

  elif opcao == "s": 
    #saque 
    if saque_limite > 0:
      print(f"o seu saldo atual é de R${format(saldo,'.2f')} \n\n")
      saque = float(input("quanto você deseja sacar: "))
      if saque <= 500.00:
        if saldo > saque:
          extrato += (f"O valor sacado foi: R${format(saque,'.2f')} \n") 
          saque_limite-= 1
          saldo-= saque
        else:
          print("\n\n--------Saldo Insuficiente------------")
          retorno = input("voltar para o menu ? [s][n]")
          sistema = True if retorno == 's' else False
      else:
        print("\n\n--------Saque acima do limite permitido------------")
        retorno = input("\nvoltar para o menu ? [s][n]")
        sistema = True if retorno == 's' else False
    else:
      print("\n----------limite de saque diario atingido----------\n")
      retorno = input("voltar para o menu ? [s][n]")
      sistema = True if retorno == 's' else False
  elif opcao == "e":
    if extrato == '':
      print("\n----------Extrato----------\n")
      print("Não foram realizados movimentos")
      print("\n---------------------------\n")

    else:
      print("\n----------Extrato----------\n")
      print(extrato)
      print(f"Saldo total: R${format(saldo,'.2f')}")
      print("\n---------------------------\n")

  elif opcao == "n":
    break
  else:
    print("\n------------comando invalido------------")


