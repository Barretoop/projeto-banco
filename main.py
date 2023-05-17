import conta
import clienteB
import especial


def exibir_menu():
    print("====                                        ====")
    print("====                                        ====")
    print("==== Banco Do Desenvolvimento Universitario ====")
    print("====                                        ====")
    print("====                                        ====")
    print("1. Cadastrar cliente")
    print("2. Alterar cliente")
    print("3. Consultar cliente")
    print("4. Remover cliente")
    print("5. Cadastrar conta")
    print("6. Cadastrar conta especial")
    print("7. Consultar saldo")
    print("8. Realizar depósito")
    print("9. Realizar saque")
    print("10. Consultar extrato")
    print("0. Sair")


while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        clienteB.cadastrar_cliente()
    elif opcao == "2":
        clienteB.alterar_cliente()
    elif opcao == "3":
        clienteB. consultar_cliente()
    elif opcao == "4":
        clienteB. remover_cliente()
    elif opcao == "5":
        clienteB.cadastrar_conta()
    elif opcao == "6":
        especial.cadastrar_conta_especial()
    elif opcao == "7":
        conta.consultar_saldo()
    elif opcao == "8":
        conta.realizar_deposito()
    elif opcao == "9":
        conta.realizar_saque()
    elif opcao == "10":
        conta.consultar_extrato()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
