from random import shuffle


# Função que abre o arquivo txt
def open_text_file():
    
    # Abre o documento de texto
    with open('list_names.txt', 'r') as file:
        
        # Insere o conteúdo do documento em uma lista, onde cada linha será um elemento
        content = file.read().split()
        
    # Retorna uma lista contendo elementos do arquivo txt
    return content
    
 
# Função responsável pela "divisão" dos grupos
def division(n_grups, list_persons):
    
    # Tamanho dos "grupos" será o resultado da divisão inteira da operação:
    # quantidade de pessoas contidas no documento txt 
    # dividido pela quantidade de grupos informado pelo usuário
    group_size = len(list_persons) // n_groups
    
    # Embaralha os itens de "list_persons"
    shuffle(list_persons)
    
    # groups recebe uma lista criada por um list comprehension 
    # Inicia com um loop for de 0 até o tamamho de "list_persons", pulando de "group_size" em "group_size"
    # Estamos percorendo em pedaços com o tamanho de "group_size"
    # Por fim, estamos pegando o elemento contido na em "list_persons" iniciando em "indice" 
    # até "indice" + "group_size" do loop for
    # Se houver sobra na divisão de list_persons, a última lista terá menos elementos.
    groups = [list_persons[indice:indice+group_size] for indice in range(0, len(list_persons), group_size)]
    
    return groups
    
    
# Variável recebendo a função que abre o arquivo txt
txt = open_text_file()

while True:
    
    n_groups = input('Digite a quantidade de grupos desejada: ').strip()
    
    # Validação retornando "True" caso "n_groups" conter apenas números
    # E se for "n_groups" for diferente de 0
    if n_groups.isdecimal() and n_groups != '0' and int(n_groups) <= len(txt):
        
        # Transforma em um número inteiro
        n_groups = int(n_groups)
        
        # Sair do loop
        break
    
    print('=> Digite um NÚMERO INTEIRO válido!\n'
          '=> O número de grupos NÃO pode ser maior que a quantidade de pessoas cadastrada no arquivo "txt"\n'
          '=> O número deve ser MAIOR que ZERO\n')
    

# Variável recebendo a função onde será feita a divisão dos "grupos"
# Essa variável irá conter uma lista com listas de cada "grupo"
groups = division(n_groups, txt)

for i, group in enumerate(groups):
    print(f'Grupo {i+1}:')
    for person in group:
        print(person)
    print()

