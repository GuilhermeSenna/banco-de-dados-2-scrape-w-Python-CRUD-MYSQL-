import mysql.connector
import matplotlib.pyplot as plt
from time import sleep

mydb = mysql.connector.connect(
    host="localhost",
    user="python",
    password="12345",
    database="saladeaula"
)


mycursor = mydb.cursor()

TUPLAS = 395

# Criando dicionarios e Lista
argumentos = []

sexo = dict()
sexo['M'] = 0
sexo['F'] = 0

idade = dict()
idade[15] = 0
idade[16] = 0
idade[17] = 0
idade[18] = 0
idade[19] = 0
idade[20] = 0
idade[21] = 0

endereco = dict()
endereco['U'] = 0
endereco['R'] = 0

familia = dict()
familia['GT3'] = 0
familia['LE3'] = 0

tempo_viagem = dict()
tempo_viagem[1] = 0
tempo_viagem[2] = 0
tempo_viagem[3] = 0
tempo_viagem[4] = 0

tempo_estudo = dict()
tempo_estudo[1] = 0
tempo_estudo[2] = 0
tempo_estudo[3] = 0
tempo_estudo[4] = 0

materias_perdidas = dict()
materias_perdidas[0] = 0
materias_perdidas[1] = 0
materias_perdidas[2] = 0
materias_perdidas[3] = 0

reforco = dict()
reforco['no'] = 0
reforco['yes'] = 0

pagar = dict()
pagar['no'] = 0
pagar['yes'] = 0

extra = dict()
extra['no'] = 0
extra['yes'] = 0

superior = dict()
superior['no'] = 0
superior['yes'] = 0

internet = dict()
internet['no'] = 0
internet['yes'] = 0

namoro = dict()
namoro['no'] = 0
namoro['yes'] = 0

rel_familia = dict()
rel_familia[1] = 0
rel_familia[2] = 0
rel_familia[3] = 0
rel_familia[4] = 0
rel_familia[5] = 0

tempo_livre = dict()
tempo_livre[1] = 0
tempo_livre[2] = 0
tempo_livre[3] = 0
tempo_livre[4] = 0
tempo_livre[5] = 0

vida_social = dict()
vida_social[1] = 0
vida_social[2] = 0
vida_social[3] = 0
vida_social[4] = 0
vida_social[5] = 0

saude = dict()
saude[1] = 0
saude[2] = 0
saude[3] = 0
saude[4] = 0
saude[5] = 0

faltas = dict()
faltas['0-9'] = 0
faltas['10-19'] = 0
faltas['20-29'] = 0
faltas['30-39'] = 0
faltas['40-49'] = 0
faltas['50-59'] = 0

# TUPLAS = 187
# TUPLAS = 208

WHERE = False

if not WHERE:
    mycursor.execute("SELECT * FROM estudante ")

    myresult = mycursor.fetchall()
else:
    restricao = "WHERE namoro='yes'"
    mycursor.execute("SELECT count(ID) FROM estudante " + restricao)

    myresult = mycursor.fetchall()

    if myresult:
        for x in myresult:
            TUPLAS = x[0]

    mycursor.execute("SELECT * FROM estudante " + restricao)

    myresult = mycursor.fetchall()

print(TUPLAS)


# for v in sexo:
#   print(v)

if myresult:
    for x in myresult:
        for y in sexo:  # Contabilizando sexo
            if x[1] == y:
                sexo[y] += 1
                break
        for y in idade:  # Contabilizando idade
            if x[2] == y:
                idade[y] += 1
                break
        for y in endereco:  # Contabilizando endereco
            if x[3] == y:
                endereco[y] += 1
                break
        for y in familia:  # Contabilizando familia
            if x[4] == y:
                familia[y] += 1
                break
        for y in tempo_viagem:  # Contabilizando tempo de viagem
            if x[5] == y:
                tempo_viagem[y] += 1
                break
        for y in tempo_estudo:  # Contabilizando tempo de estudo
            if x[6] == y:
                tempo_estudo[y] += 1
                break
        for y in materias_perdidas:  # Contabilizando materias perdidas
            if x[7] == y:
                materias_perdidas[y] += 1
                break
        for y in reforco:           # Contabilizando Reforço
            if x[8] == y:
                reforco[y] += 1
                break
        for y in pagar:             # Contabilizando Pagar materias
            if x[9] == y:
                pagar[y] += 1
                break
        for y in extra:             # Contabilizando Extracurriculares
            if x[10] == y:
                extra[y] += 1
                break
        for y in superior:          # Contabilizando Ensino superior
            if x[11] == y:
                superior[y] += 1
                break
        for y in internet:          # Contabilizando internet
            if x[12] == y:
                internet[y] += 1
                break
        for y in namoro:            # Contabilizando namoro
            if x[13] == y:
                namoro[y] += 1
                break
        for y in rel_familia:       # Contabilizando relacionamento com a familia
            if x[14] == y:
                rel_familia[y] += 1
                break
        for y in tempo_livre:       # Contabilizando tempo livre pós aula
            if x[15] == y:
                tempo_livre[y] += 1
                break
        for y in vida_social:       # Contabilizando Vida social
            if x[16] == y:
                vida_social[y] += 1
                break
        for y in saude:             # Contabilizando saude
            if x[17] == y:
                saude[y] += 1
                break
        if 0 <= x[18] < 10:   # Contabilizando Nº de faltas
            faltas['0-9'] += 1
        elif 10 <= x[18] < 20:
            faltas['10-19'] += 1
        elif 20 <= x[18] < 30:
            faltas['20-29'] += 1
        elif 30 <= x[18] < 40:
            faltas['30-39'] += 1
        elif 40 <= x[18] < 50:
            faltas['40-49'] += 1
        else:
            faltas['50-59'] += 1

argumentos = {'sexo': sexo,
              'idade': idade,
              'endereco': endereco,
              'familia': familia,
              'tempo de viagem': tempo_viagem,
              'tempo de estudo': tempo_estudo,
              'materias perdidas': materias_perdidas,
              'reforco': reforco,
              'pagar': pagar,
              'extra': extra,
              'superior': superior,
              'internet': internet,
              'namoro': namoro,
              'relacao familia': rel_familia,
              'tempo livre': tempo_livre,
              'vida social': vida_social,
              'saude': saude,
              'faltas': faltas}

grupos = []
valores = []

for name, dict_ in argumentos.items():
    print(f'\n{name}')
    grupos.clear()
    valores.clear()

    for pos, arg in dict_.items():
        # grupos.append(pos)
        print(f'{pos} -> {(arg/TUPLAS) * 100:.2f}%')

    # for pos, arg in dict_.items():
    #     valores.append(float(f'{(arg/TUPLAS) * 100:.2f}'))
        # print(f'{pos} -> {(arg/TUPLAS) * 100:.2f}%')

    # plt.title(name)
    # plt.bar(grupos, valores)
    # plt.show()
