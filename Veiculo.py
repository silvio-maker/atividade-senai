#Silvio, Luiz
class Veiculo:
    def __init__(self, marca, modelo, ano, valor):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self._valor = valor

    def calcular_ipva(self):
        pass

    def __str__(self):
        return f"{self._ano} {self._marca} {self._modelo} - R${self._valor:.2f}"


class Carro(Veiculo):
    def calcular_ipva(self):
        return self._valor * 0.04


class Moto(Veiculo):
    def calcular_ipva(self):
        return self._valor * 0.02


class Caminhao(Veiculo):
    def calcular_ipva(self):
        return self._valor * 0.01


def menu():
    veiculos = []
    while True:
        print("\nMenu:")
        print("1. Cadastrar veículo")
        print("2. Consultar veículo")
        print("3. Calcular IPVA")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo = input("Digite o tipo do veículo (Carro, Moto, Caminhão): ").strip().lower()
            marca = input("Digite a marca: ")
            modelo = input("Digite o modelo: ")
            ano = input("Digite o ano: ")
            valor = float(input("Digite o valor: R$"))

            if tipo == "carro":
                veiculo = Carro(marca, modelo, ano, valor)
            elif tipo == "moto":
                veiculo = Moto(marca, modelo, ano, valor)
            elif tipo == "caminhão":
                veiculo = Caminhao(marca, modelo, ano, valor)
            else:
                print("Tipo de veículo inválido!")
                continue

            veiculos.append(veiculo)
            print("Veículo cadastrado com sucesso!")

        elif opcao == "2":
            print(veiculo)
        elif opcao == "3":
            if  veiculos=='':
                print("Nenhum veículo cadastrado.")
                

            ipva = veiculo.calcular_ipva()
            print(f"IPVA do veículo {veiculo}: R${ipva:.2f}")
           

        elif opcao == "4":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Chamada para executar o menu
if __name__ == "__main__":
    menu()