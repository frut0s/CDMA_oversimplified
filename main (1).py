def bit_request(): #requisita listas de bits baseado no número de nós (no caso do projeto tem que ser 2). armazena ambas informação em diferentes listas
    number_of_hosts = int(input("Quantos nós há? "))
    bits_hosts_data = []

    for i in range(1, number_of_hosts + 1): #utilizando a informação de quantos nós há, requisita a lista de bits para cada nó. faz isso utilizando a função range, que cria uma sequência de números baseada no número de hosts. porque o último item do range costuma ser ignorado, tive que adicionar +1 para que o resultado não viesse com o último número sempre faltando. isso é algo do python. incrementalmente pergunta qual a lista de bits de cada host
        user_input = input(f"Bits para cada nó {i}, separados por espaço (apenas 1 ou -1, devem ser 8 bits)\n")
        bits = [int(nbits) for nbits in user_input.split()]

        # se o comprimento da lista bits for diferente de 8 informa erro
        if len(bits) != 8:
            print("Erro: Insira 8 bits.")
            return None

        # se o input for diferende de 1 ou -1, mostra erro 
        if all(bit in [-1, 1] for bit in bits):
            bits_hosts_data.append(bits)
        else:
            print("Erro: Bits devem ter valor 1 ou -1.")
            return None

    return bits_hosts_data  #retorna uma lista de listas contendo os bits 

def multiply_bits_with_codes(bits_hosts_data, codes):
    multiplied_bits = {} #define um dicionário chamado "bits multiplicados"

    for i, bits_list in enumerate(bits_hosts_data, start=1): #enumerate itera sobre os elementos da lista enquanto rastreia o índice do elemento. cria uma string de nome  Nó e número n incremental dependendo no número do índice.
        host_name = f"Nó{i}"
        code = codes[i - 1]  #subtração é necessária pois contagem em python começa do 1, enquando índices começam do 0 

        # confirma que ambas listas  têm 8 elementos 
        if len(bits_list) != 8 or len(code) != 8:
            print("Erro: Ambos devem ter exatamente 8 elementos.")
            return None

        multiplied_bits[host_name] = [[bit * code_val for code_val in code] for bit in bits_list] #para cada bit na lista de bits, itera sobre o elemento correspondente na lista de códigos, multiplica os elementos correspondentes, e cria uma lista bidimencional com os resultados. após isso, associa as listas criadas ao nome "host"(nó). resultado 1 é associado a host 1, assim vai.

    return multiplied_bits #retorna um dicionário 

def organize_bits_into_chips(multiplied_bits_result): #recebe o dicionário multiplied_bits como argumento, e insere o valor de bits de cada host do dicionário a uma lista vazia chamada "chips". itera, criando uma nova lista, para cada host do dicionário.
    chips = []

    for host, bits_list in multiplied_bits_result.items(): #host é o nome de cada nó. para cada host no dicionário
        chips.append(bits_list) #injeta a o item bits_listen do dicionário (que na realidade não são mais bits) a uma lista chamada chips

    return chips #retorna lista de  chips 

def sum_chips(chip1, chip2):
    sum_chips_result = [] #cria lista chamada "resultado da soma dos chips"

    for bits_list1, bits_list2 in zip(chip1, chip2): #zip é uma funçao do python que facilita iterar sobre duas litas ao mesmo tempo. ele pega o primeiro elemento de ambas listas e faz algo, depois o segundo, etc.
        sum_list = [bit1 + bit2 for bit1, bit2 in zip(bits_list1, bits_list2)] #cria lista sum_list que contem a soma elemento por elementos de cada bit list
        sum_chips_result.append(sum_list)

    return sum_chips_result # : retorna a lista sum_chips_result contendo as listas de bits resultantes da soma para cada nó


bits_hosts_data_stored = bit_request() #chama a funçao bit request e guarda na variável 
if bits_hosts_data_stored is not None:
    codes_list = [  #crima uma lista de listas chamada codes_list que contém códigos específicos associados a cada nó
        [1, 1, 1, -1, 1, -1, -1, -1],
        [1, -1, 1, 1, 1, -1, 1, 1]
    ]  

    multiplied_bits_result = multiply_bits_with_codes(bits_hosts_data_stored, codes_list) #Chama a função multiply_bits_with_codes passando os bits dos nós, e os códigos associados. multiplica cada bit pelo código correspondente para cada nó e retorna um dicionário chamado multiplied_bits_result.


    chips = organize_bits_into_chips(multiplied_bits_result)# organizar os bits multiplicados em "chips"
    print("\nChips:")
    for i, chip in enumerate(chips, start=1): #itera sobre a lista de "chips" usando enumerate pega o índice e o chip correspondente.
        print(f"Chip{i}: {chip}") #imprime a exibição dos "chips".


    chips_sum_result = sum_chips(chips[0], chips[1]) #chama a funçao some-chips. os chips são sub-listas de Chips, 0 marca o índice da primeira sub-lista e 1 o da segunda.

 
    print("Soma:", chips_sum_result)
    
    #cria duas listas com o mesmo conteúdo, ambas são cópias do resultado da soma
chips_sum_code1 = chips_sum_result.copy()
chips_sum_code2 = chips_sum_result.copy()


# re-define os códigos pois tive dificuldade em utilizar a outra definição que fiz anteriormente...
factor_code1 = [1, 1, 1, -1, 1, -1, -1, -1]
factor_code2 = [1, -1, 1, 1, 1, -1, 1, 1]

# multiplica os elementos da primeira lista pelo elemento correspondente da code1
for i, chip in enumerate(chips_sum_code1):
    chips_sum_code1[i] = [bit * factor for bit, factor in zip(chip, factor_code1 * len(chips_sum_code1))]

# mesma coisa para para a segunda lista. nesse ponto já cansei de usar For incremental
for i, chip in enumerate(chips_sum_code2):
    chips_sum_code2[i] = [bit * factor for bit, factor in zip(chip, factor_code2 * len(chips_sum_code2))]

# mostra resultado
print("\nChips Sum Code 1:", chips_sum_code1)

print("\nChips Sum Code 2:", chips_sum_code2)


# funçao que soma todos os items
def sum_chip_values(chips):
    sum_chips_values_result = [] #cria uma nova lista que conterá o resultado da soma

    for chip in chips: #para cada chip em chips, resultado da soma da lista inteira será atribuida  á lista "chips soma"
        chip_sum = sum(chip)
        sum_chips_values_result.append([chip_sum]) #enfia o resultado na lista sum_chips_values_result

    return sum_chips_values_result

#separa ambas em duas variáveis distintas
sum_values_code1 = sum_chip_values(chips_sum_code1)
sum_values_code2 = sum_chip_values(chips_sum_code2)


print("\nSoma dos chips do nó 1:", sum_values_code1)

print("\nSoma dos chips do nó 2:", sum_values_code2)

    
    
def divide_chip_values(chips): #função que divide cada item de cada lista por 8
    divided_chips_values_result = []

    for chip in chips:
        divided_chip = [value / 8 for value in chip]
        divided_chips_values_result.append(divided_chip) #enfia o resultado em uma nova lista

    return divided_chips_values_result #retorna a tal lista


divided_values_code1 = divide_chip_values(sum_values_code1)
divided_values_code2 = divide_chip_values(sum_values_code2) #chama a funçao
2

def convert_to_bits(chips): #converte os valores de float para inteiro (divisões costumam ter resultado em float no python)
    bits_result = []

    for chip in chips:
        bits_chip = [int(round(value)) for value in chip]
        bits_result.append(bits_chip) #enfia tudo em uma nova lista chamada bits result

    return bits_result

#chama a função
bits_code1 = convert_to_bits(divided_values_code1)
bits_code2 = convert_to_bits(divided_values_code2)

#confirma mais uma vez que os valores são inteiros 
bits_code1 = [[int(bit) for bit in chip] for chip in bits_code1]
bits_code2 = [[int(bit) for bit in chip] for chip in bits_code2]

# Print the results
print("\nBits do nó 1:", bits_code1)

print("\nBits do nó 2:", bits_code2)