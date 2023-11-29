from random import randint

_NOMES = [
    "Ana", "Beatriz", "Carolina", "Daniela", "Eduarda", "Fernanda", "Gabriela", "Helena", "Isabela", "Juliana",
    "Larissa", "Mariana", "Natália", "Olívia", "Patrícia", "Renata", "Sofia", "Tatiane", "Valentina", "Yasmin",
    "Amanda", "Bianca", "Clara", "Débora", "Elaine", "Franciele", "Giovana", "Heloísa", "Izabella", "Jéssica",
    "Kamila", "Lívia", "Mirella", "Nathália", "Ornella", "Priscila", "Raquel", "Samara", "Talita", "Ursula",
    "Vitória", "Wanessa", "Ximena", "Yara", "Zuleika", "André", "Bruno", "Carlos", "Diego", "Eduardo", "Fábio", 
    "Gustavo", "Henrique", "Igor", "João", "Lucas", "Matheus", "Nathan", "Otávio", "Pedro", "Rafael", "Sérgio", 
    "Thiago", "Vinícius", "William", "Alexandre", "Bernardo", "César", "Davi", "Enzo", "Felipe", "Gabriel", 
    "Heitor", "Isaac", "Joaquim", "Kaique", "Leandro", "Miguel", "Nicolas", "Otto", "Paulo", "Ricardo", "Santiago", 
    "Thales", "Ulisses", "Vitor", "Wagner", "Xavier", "Yago", "Zélio", "Adriano", "Breno", "Caio", "Daniel"]


_DISCIPLINAS = ["MATEMÁTICA", "PORTUGUÊS", "HISTÓRIA", "GEOGRAFIA", "CIÊNCIAS", "FÍSICA", "QUÍMICA", "BIOLOGIA", 
                "INGLÊS", "EDUCAÇÃO FÍSICA", "ARTES", "FILOSOFIA", "SOCIOLOGIA", "ESPANHOL", "FRANCÊS", "LITERATURA", 
                "REDAÇÃO", "MÚSICA", "TECNOLOGIA DA INFORMAÇÃO", "EDUCAÇÃO AMBIENTAL"]


class Randomization:        
    def _new_name() -> str:
        """RETORNA NOME ALEATÓRIO"""
        return _NOMES[randint(0,30)]

    def _new_idade_aluno() -> int:
        """RETORNA IDADE ENTRE 10 E 20"""
        return randint(10,20)

    def _new_idade_prof() -> int:
        """RETORNA IDADE ENTRE 20 E 70"""
        return randint(20,70)

    def _new_matricula() -> int:
        """RETORNA MATRÍCULA ENTRE 100 E 100000"""
        return randint(100,100000)

    def _new_subject() -> str:
        """RETORNA DISCIPLINA ALEATÓRIA"""
        return _DISCIPLINAS[randint(0,19)]

    def _new_carga_horaria() -> int:
        """RETORNA CARGA HORÁRIA"""
        while True:
            aux = randint(20, 200)
            if aux%5==0:
                return aux


class Dados:
    def __init__(self) -> None:
        self._dados_alunos = []
        self._dados_professores = []
        self._dados_disciplinas = []
        self._dados_turmas = []
        self._random = Randomization

    def cria_alunos(self, qtd:int) -> list:
        """CRIA ALUNOS"""
        for i in range(qtd):
            aluno = {'nome': self._random._new_name(), 'idade': self._random._new_idade_aluno(), 'matricula': self._random._new_matricula()}
            self._dados_alunos.append(aluno)
            i-=1
        return self._dados_alunos

    def cria_professores(self, qtd:int) -> list:
        """CRIA PROFESSORES"""
        for j in range(qtd):
            prof = {'nome': f'Prof. {self._random._new_name()}', 'idade': self._random._new_idade_prof(), 'cod': self._random._new_matricula()}
            self._dados_professores.append(prof)
            j-=1
        return self._dados_professores

    def cria_disciplinas(self, qtd:int) -> list:
        """CRIA DISCIPLINAS"""        
        for k in range(qtd):
            subject = {'nome': self._random._new_subject(), 'carga_horaria': self._random._new_carga_horaria()}
            self._dados_disciplinas.append(subject)
            k-=1
        return self._dados_disciplinas

    def cria_turmas(self) -> list:
        """CRIA TURMAS"""
        for disc in self._dados_disciplinas:
            turma = {'codigo': self._random._new_matricula(), 'disciplina': disc} 
            self._dados_turmas.append(turma)
        return self._dados_turmas