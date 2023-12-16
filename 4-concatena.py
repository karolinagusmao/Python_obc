name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n")) #\n quebra a linha
gamePrice = float(input("Digite o preço do jogo\n"))
planIncluded = input("Está incluso no serço mensal?\n")

print("###Dados do Jogo###")
print("-------------------")

# Alternativa 1
# print("Nome do Jogo: ", name)
# print("Ano do Jogo: ", yearLaunch)
# print("Preçoe do Jogo: ", gamePrice)
# print("Está incluso no plano? ", planIncluded)

# Alternativa 2
# print(f"Nome do Jogo: ", name, 
#       "\n Ano de lançamento: ", yearLaunch,
#       "\n Preço: ", gamePrice, 
#       "\n Plano mensal? ", planIncluded)

#Alternativa 3 - mais atual no python
print(f"Nome do Jogo: {name} \n Ano Lançamento: {yearLaunch} \n Preço: {gamePrice} \n Plano mensal? {planIncluded} \n")
