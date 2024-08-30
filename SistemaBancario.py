opcao = 0

saldo = 0
saques_diario = 0
LIMITE_SAQUE = 3
saque_max = 500
extrato = ''

while opcao != 5:
    print('''=====Ensira o numero da operação desejada=====
    1- Deposito
    2- Saque
    3- Extrato
    5- Sair
===============================================''')
    
    opcao = int(input("Digite sua opção: "))
    
    if opcao == 1:
        deposito = float(input("Digite o valor do deposito: \n"))

        if deposito > 0:
                saldo =+ deposito
                extrato += f"Depisito: R$ {deposito:.2f}\n"
        else:
             print("Impossivel fazer deposito de valores menores ou iguais a 0\n")

    elif opcao == 2:
          if saques_diario < LIMITE_SAQUE:
               saque = float(input("Digite o valor que deseja sacar: "))
              
               execedeu_saldo = saque > saldo

               excedeu_limite = saque > saque_max

               if execedeu_saldo:
                   print("Saldo insuficiente para o saque.")

               elif excedeu_limite:
                   print("Valor de saque execedeu o limite")

               elif saque > 0:
                    saldo -= saque
                    extrato += f"Saque: R$ {saque:.2f}\n"
                    saques_diario += 1
          else:
              print("Quantidade de saques maximos ja realiazados!\n")
         
    elif opcao == 3:
          print (f"============ EXTRATO ============")
          print ("Não foram reaalizadas movimentações." if not extrato else extrato)
          print("\n Saldo: R$ {saldo:.2f}")
          print("=================================\n")

    elif opcao == 5:
         print("Encerrando Aplicativo\n")
         break
    else:
        print("Opção invalida, verifique a opção selecionada e as disponisveis")

