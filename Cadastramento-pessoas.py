cores = {'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m',
         'violeta': '\033[1;35m',
         'clear': '\033[m'}
pessoa = dict()
lista = list()
lista_mulheres = list()
lista_idade_maior_media = list()
media = 0
while True:
    pessoa["Nome"] = str(input("Digite o nome: "))
    pessoa["Sexo"] = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
    pessoa["Idade"] = int(input("Digite a idade: "))
    pessoa_copia = pessoa.copy()    # Realiza uma copia para que, na "lista", não fique dados duplicados
    lista.append(pessoa_copia)      
    media += pessoa["Idade"]        # Comando para realiza a media de idade de todas pessoas cadastradas
    if pessoa["Sexo"] in 'F':
        lista_mulheres.append(pessoa["Nome"])
    continuar = str(input(f"Deseja adicionar outra pessoa [S/N]? ")).upper().strip()[0]
    while continuar not in "SN":
        continuar = str(input("Comando inválido! Deseja adicionar outra pessoa [S/N]}?  ")).strip().uppper()[0]
    if continuar in 'N':    
        print()
        break
for c in lista:     # Retornar todos os dicionários presentes na "lista"
    print('-=' * 10)
    for k, v in c.items():      # c.items pega os dados dos dicionários retornados na linha 20)
        print(f"O(a) {k} é {cores['verde']}{v}{cores['clear']}")
    print('-=' * 10)
media_idade = int(media / len(lista))
for x in lista:
    if x["Idade"] > media_idade:        # Se no dicionário, o elemento "Idade" for maior que media_idade executar linha 29
        lista_idade_maior_media.append(x["Nome"])
print(f"\nNa lista, tivemos {cores['vermelho']}{len(lista)}{cores['clear']} pessoas cadastradas")
print(f"A média de idade das pessoas é: {media_idade}")
if len(lista_mulheres) > 0:
    print(f"A lista com todas as mulheres é:")
    for k in lista_mulheres:
        print(f"- {cores['violeta']}{k}{cores['clear']}")
if len(lista_idade_maior_media) > 0:
    print(f"A lista com todas as pessoas com a idade maior que a média é:")
    for k in lista_idade_maior_media:
        print(f"- {cores['azul']}{k}{cores['clear']}")