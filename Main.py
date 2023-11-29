from Escola import *
from Util import * 

def main(nome_escola, qtd_alunos, qtd_professores, qtd_disciplinas) -> str:
    # INSTANCIA UMA NOVA ESCOLA
    escola_upf = Escola(nome_escola)

    # CRIA DADOS FICTÍCIOS
    data = Dados()
    alunos = data.cria_alunos(qtd=qtd_alunos)
    professores = data.cria_professores(qtd=qtd_professores)
    disciplinas = data.cria_disciplinas(qtd=qtd_disciplinas)
    turmas = data.cria_turmas()

    # ADICIONA ALUNO NA ESCOLA
    for aluno in alunos:
        escola_upf.adicionar_aluno(aluno)

    # ADICIONA PROFESSOR NA ESCOLA
    for prof in professores:
        escola_upf.adicionar_professor(prof)

    # ADICIONA DISCIPLINA NA ESCOLA
    for d in disciplinas:
        escola_upf.adicionar_disciplina(d)

    count = 0
    for turma in turmas:
        if count >= len(escola_upf.professores):
            count = 0

        # ADICIONA TURMA NA ESCOLA
        t = escola_upf.adicionar_turma(turma)
        
        # DESIGNA UM PROFESSOR PARA A TURMA
        t.designar_professor(escola_upf.professores[count])
        count += 1

        # ADICIONA ALUNOS NAS TURMAS
        if t.codigo%2==0:
            metade_fim_alunos = escola_upf.alunos[:int((len(escola_upf.alunos)/2))]
            for aluno in metade_fim_alunos:
                t.matricular_aluno(aluno)   
        else:
            comeco_metade_alunos = escola_upf.alunos[int((len(escola_upf.alunos)/2)):]
            for aluno in comeco_metade_alunos:
                t.matricular_aluno(aluno)

    # INSTANCIA NOVO RELATORIO
    relatorio = Relatorio(escola_upf)
    
    # PRINTA DADOS DA ESCOLA
    relatorio.get_data()

    # RETORNA MENSAGEM DE SUCESSO
    return f'\n\n{nome_escola.upper()} CRIADO(A) COM SUCESSO\n\n'

print(main('ESCOLA SANANDUVA', 40, 7, 13))
print(main('ESCOLA RONDA ALTA', 50, 9, 15))
print(main('ESCOLA PASSO FUNDO', 75, 10, 18))