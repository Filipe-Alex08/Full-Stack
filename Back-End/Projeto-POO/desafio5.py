materias = {

    'Português': {},
    'Matemática': {},
    'História': {}
}

for materia in materias:
    
    print("Matéria: ", materia)

    while True:

        aluno = input('Digite nome do aluno: ')

        if aluno == '':
            break

        nota = float(input('Digite nota do aluno: '))

        materias[materia][aluno] = nota

minimo = float(input('Digite o mínimo para passar: '))

alunos_port = set(materias['Português'].keys())
alunos_mat = set(materias['Matemática'].keys())
alunos_hist = set(materias['História'].keys())

alunos_inter = alunos_port & alunos_mat & alunos_hist

passaram = []

for aluno in alunos_inter:

    passou = True

    for materia in materias.values():

        if materia[aluno] < minimo:
            passou = False
            break

    if passou:
        passaram.append(aluno)

print('Os alunos que passaram foram: ', passaram)

