class Disciplina:
    def __init__(self, nome:str, carga_horaria:int) -> None:
        self.nome_disciplina = nome
        self._carga_horaria = carga_horaria

    def exibir_informacoes(self) -> str:
        """EXIBE NOME E CARGA HORÁRIA DA DISCIPLINA"""
        print(f"Disciplina: {self.nome_disciplina} || Carga Horária: {self._carga_horaria} horas\n")


class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
        self.nome = nome
        self.idade = idade


# CLASSE ALUNO HERDA PESSOA
class Aluno(Pessoa):
    def __init__(self, nome:str, idade:int, matricula:int) -> None:
        super().__init__(nome, idade)
        self._matricula = matricula
        self._disciplinas_matriculadas = []

    def matricular(self, disciplina:Disciplina) -> None:
        """MATRICULA ALUNO EM UMA DISCIPLINA"""
        self._disciplinas_matriculadas.append(disciplina)

    def exibir_informacoes(self) -> str:
        """EXIBE NOME, MATRÍCULA, IDADE E AS DISCIPLINAS MATRICULADAS DO ALUNO"""
        print(f"Aluno: {self.nome} || Matrícula: {self._matricula} || Idade: {self.idade} || Disciplinas: {self._disciplinas_matriculadas}\n")



# CLASSE PROFESSOR HERDA PESSOA
class Professor(Pessoa):
    def __init__(self, nome:str, idade:int, codigo_funcionario:int) -> None:
        super().__init__(nome, idade)
        self._codigo_funcionario = codigo_funcionario
        self._disciplinas_ministradas = []

    def ministrar_disciplina(self, disciplina:Disciplina) -> None:
        """DESIGNA PROFESSOR PARA A DISCIPLINA"""
        self._disciplinas_ministradas.append(disciplina)

    def exibir_informacoes(self) -> str:
        """EXIBE NOME, CODIGO E DISCIPLINAS MINISTRADAS DO PROFESSOS"""
        print(f"Professor: {self.nome} || Código: {self._codigo_funcionario} || Disciplinas: {self._disciplinas_ministradas}\n")


class Turma:
    def __init__(self, codigo:int, disciplina:Disciplina) -> None:
        self.codigo = codigo
        self.disciplina = disciplina
        self.professor = ''
        self._alunos_matriculados = []

    def matricular_aluno(self, aluno:Aluno) -> None:
        """MATRICULA ALUNO NA DISCIPLINA"""
        self._alunos_matriculados.append(aluno.nome)
        aluno.matricular(self.disciplina)

    def designar_professor(self, professor:Professor) -> None:
        """DESIGNA UM PROFESSOR PARA A DISCIPLINA"""
        self.professor = professor.nome
        professor.ministrar_disciplina(self.disciplina)

    def exibir_informacoes(self) -> str:
        """EXIBE CODIGO. NOME, PROFESSOR E ALUNOS DA DISCIPLINA"""
        print(f"Turma {self.codigo} - {self.disciplina} || Professor: {self.professor} || Alunos: {self._alunos_matriculados}\n")


class Escola:
    def __init__(self, nome:str) -> None:
        self.nome = nome
        self.alunos = []
        self.professores = []
        self.disciplinas = []
        self.turmas = []

    def adicionar_aluno(self, dados_aluno:dict) -> None:
        """ADICIONA ALUNO NA ESCOLA"""
        try:
            self.alunos.append(Aluno(dados_aluno['nome'], dados_aluno['idade'], dados_aluno['matricula']))
        except Exception:
            raise Exception

    def adicionar_professor(self, dados_professor:dict) -> None:
        """ADICIONA PROFESSOR NA ESCOLA"""
        try:
            self.professores.append(Professor(dados_professor['nome'], dados_professor['idade'], dados_professor['cod']))
        except Exception:
            raise Exception

    def adicionar_disciplina(self, dados_disciplina:dict) -> None:
        """ADICIONA DISCIPLINA NA ESCOLA"""
        try:
            self.disciplinas.append(Disciplina(dados_disciplina['nome'], dados_disciplina['carga_horaria']))
        except Exception:
            raise Exception

    def adicionar_turma(self, dados_turma:dict) -> Turma:
        """ADICIONA TURMA NA ESCOLA"""
        turma = Turma(dados_turma['codigo'], dados_turma['disciplina']['nome'])
        self.turmas.append(turma)
        return turma


class Relatorio:
    def __init__(self, escola:Escola) -> None:
        self._escola = escola

    def get_alunos(self) -> None:
        # PRINTANDO ALUNOS
        print("Alunos matriculados:")
        for aluno in self._escola.alunos:
            aluno.exibir_informacoes()

    def get_professores(self) -> None:
        # PRINTANDO PROFESSORES
        print("\nProfessores:")
        for professor in self._escola.professores:
            professor.exibir_informacoes()
    
    def get_disciplinas(self) -> None:
        # PRINTANDO DISCIPLINAS
        print("\nDisciplinas:")
        for disciplina in self._escola.disciplinas:
            disciplina.exibir_informacoes()
    
    def get_turmas(self) -> None:
        # PRINTANDO TURMAS
        print("\nInformações das Turmas:")
        for turma in self._escola.turmas:
            turma.exibir_informacoes()
    
    def get_data(self) -> None:
        """EXIBE TODOS OS DADOS DA ESCOLA"""
        self.get_alunos()
        print('\n#########################################################################################################################################\n')
        self.get_professores()
        print('\n#########################################################################################################################################n')
        self.get_disciplinas()
        print('\n#########################################################################################################################################\n')
        self.get_turmas()
        print('\n#########################################################################################################################################\n')