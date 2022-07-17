from cgitb import text
from decimal import ROUND_HALF_DOWN
import math
import random
from string import punctuation

class Objeto(object):
    def __init__(self, word, vector):
        self.word = word
        self.vector = vector

class Objeto1(object):
    def __init__(self, word, vector, tipo):
        self.word = word
        self.vector = vector
        self.tipo = tipo

class Cosin(object):
    def __init__(self, word, vector, tipo, cosin):
        self.word = word
        self.vector = vector
        self.tipo = tipo
        self.cosin = cosin

class Punctuation(object):
    def __init__(self, tipo, index):
        self.tipo = tipo
        self.index = index

def input_vector():
    acao = []
    caracteristicas = []
    data = []
    evento = []
    lugar = []
    nomes = []
    objetos = []
    organizacao = []
    types = [acao, caracteristicas, data, evento, lugar, nomes, objetos, organizacao]
    files = ["acao", "caracteristicas", "data", "evento", "lugar", "nomes", "objetos", "organizacao"]
    for i in range(0, len(files)):
        f = open(f'./sinopseGenerator/vectors/vectors_{files[i]}.txt', 'r', encoding='utf-8')
        for line in f:
            splitted = line.split(' ')
            types[i].append(Objeto(word = splitted[0], vector = splitted[1].replace('\n', '')))
    return types

def convert_vectors(string):
    vector = string.replace('[', '').replace(']', '')
    vec = vector.split(',')
    
    return [int(x) for x in vec]

def dot_vectors(v1, v2):
    dot = 0
    if(len(v1) == len(v2)):
        for i in range(0, len(v1)):
            dot += v1[i] * v2[i]
        return dot

def cosin_vectors(v1, v2):
    cosin = dot_vectors(v1, v2) / (math.sqrt(dot_vectors(v1, v1)) * math.sqrt(dot_vectors(v2, v2)))
    return cosin

def create_objects():
    array = []
    tipos = ["acao", "caracteristicas", "data", "evento", "lugar", "nomes", "objetos", "organizacao"]
    for tipo in tipos:
        file = open(f'./sinopseGenerator/vectors/vectors_{tipo}.txt', 'r', encoding='utf-8')
        for line in file:
            infos = line.split(' ')
            array.append(Objeto1(word = infos[0], vector = convert_vectors(infos[1]), tipo = tipo))
    return array

def handle_input(vector):
    order_by_cosin = []
    array = create_objects()
    for item in array:
        cosin = cosin_vectors(item.vector, vector)
        order_by_cosin.append(Cosin(word = item.word, vector = item.vector, tipo = item.tipo, cosin = cosin))
    order_by_cosin.sort(key = lambda x:x.cosin, reverse = True)

    return order_by_cosin

def fill_caveirao(vector):
    array = handle_input(vector)
    olds = ["NAME", "PLACE", "CARAC", "DATE", "ORGANIZATION", "ACTION", "EVENT", "OBJECT"]
    tipos = ["nomes", "lugar", "caracteristicas", "data", "organizacao", "acao", "evento", "objetos"]
    cavs = []
    punctuation = []
    file = open(f'./sinopseGenerator/sinopse.txt', 'r', encoding='utf-8')
    for line in file:
        cavs.append(line)
    
    index = random.randint(0, len(cavs) - 1)
    choosen = cavs[index].replace('\n', '').replace('.', '').replace(',', '').replace('\'s', '').split(' ')
    print(choosen)
    original = cavs[index].split(' ')
    for i in range(0, len(original)):
        if '.' in original[i]:
            punctuation.append(Punctuation(tipo = '.', index = i))
        if ',' in original[i]:
            punctuation.append(Punctuation(tipo = ',', index = i))
        if '\'s' in original[i]:
            punctuation.append(Punctuation(tipo = '\'s', index = i))

    for i in range(0, len(tipos)):
        try:
            while choosen.index(olds[i]):
                for item in array:
                    if item.tipo == tipos[i]:
                        choosen[choosen.index(olds[i])] = item.word
                        item.tipo = "usado"
                        break
        except:
            pass
    for item in punctuation:
        choosen[item.index] += item.tipo

    return ' '.join(choosen).replace('_', ' ')