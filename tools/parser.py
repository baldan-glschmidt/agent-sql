from pathlib import Path
from markdown import MarkdownGenerator

from models import (
    Campo,
    Indice,
    Relacionamento,
    Tabela
)

class Parser:

    def __init__(self, arquivo: Path):

        self.arquivo = arquivo

        self.tabelas = []

        self.tabela_atual = None
        self.campo_atual = None
        self.indice_atual = None
        self.relacionamento_atual = None

        self.aguardando_descricao = False

    # =====================================================

    @staticmethod
    def valor_linha(linha: str) -> str:

        if ":" not in linha:
            return ""

        return linha.split(":", 1)[1].strip()

    # =====================================================

    @staticmethod
    def separar_campos(valor: str):

        if not valor:
            return []

        return [
            campo.strip()
            for campo in valor.split(";")
            if campo.strip()
        ]

    # =====================================================

    def parse(self):

        with open(
            self.arquivo,
            encoding="utf-8"
        ) as arquivo:

            for linha_original in arquivo:

                linha = linha_original.strip()

                if not linha:
                    continue

                self.processar_linha(linha)

        return self.tabelas

    # =====================================================

    def processar_linha(self, linha):

        # -------------------------------
        # NOVA TABELA
        # -------------------------------

        if linha.startswith("Tabela:"):

            self.nova_tabela(linha)

            return

        if self.tabela_atual is None:
            return

        # -------------------------------
        # DESCRIÇÃO DA TABELA
        # -------------------------------

        if self.aguardando_descricao:

            if linha.startswith("Descrição"):

                self.tabela_atual.descricao = self.valor_linha(linha)

                self.aguardando_descricao = False

            return

        # -------------------------------
        # CAMPOS
        # -------------------------------

        if linha.startswith("Nome do Campo:"):

            self.novo_campo(linha)

            return

        if self.campo_atual is not None:

            self.processar_campo(linha)

            return

        # -------------------------------
        # CHAVE PRIMÁRIA
        # -------------------------------

        if linha.startswith("Campos da Chave"):

            self.tabela_atual.chave_primaria = self.separar_campos(
                self.valor_linha(linha)
            )

            return

        # -------------------------------
        # ÍNDICES
        # -------------------------------

        if (
            linha.startswith("Nome do")
            and "Índice" in linha
        ):

            self.novo_indice(linha)

            return

        if self.indice_atual is not None:

            self.processar_indice(linha)

            return

        # -------------------------------
        # RELACIONAMENTOS
        # -------------------------------

        if linha.startswith("Relacionamento:"):

            self.novo_relacionamento(linha)

            return

        if self.relacionamento_atual is not None:

            self.processar_relacionamento(linha)

            return

    # =====================================================

    def nova_tabela(self, linha):

        self.tabela_atual = Tabela(
            nome=self.valor_linha(linha)
        )

        self.tabelas.append(self.tabela_atual)

        self.campo_atual = None
        self.indice_atual = None
        self.relacionamento_atual = None

        self.aguardando_descricao = True

    # =====================================================

    def novo_campo(self, linha):

        self.campo_atual = Campo(
            nome=self.valor_linha(linha)
        )

        self.tabela_atual.adicionar_campo(
            self.campo_atual
        )

        self.indice_atual = None
        self.relacionamento_atual = None

    # =====================================================

    def processar_campo(self, linha):

        if linha.startswith("Tipo do Campo:"):

            self.campo_atual.tipo = self.valor_linha(
                linha
            )

            return

        if linha.startswith("Permite Nulo:"):

            valor = self.valor_linha(
                linha
            ).upper()

            self.campo_atual.nulo = valor.startswith(
                "S"
            )

            return

        if linha.startswith("Descrição"):

            self.campo_atual.descricao = self.valor_linha(
                linha
            )

            self.campo_atual = None

            return

                # =====================================================

    def novo_indice(self, linha):

        self.indice_atual = Indice(
            nome=self.valor_linha(linha)
        )

        self.tabela_atual.adicionar_indice(
            self.indice_atual
        )

        self.campo_atual = None
        self.relacionamento_atual = None

    # =====================================================

    def processar_indice(self, linha):

        if linha.startswith("Tipo do Índice:"):

            self.indice_atual.tipo = self.valor_linha(
                linha
            )

            return

        if linha.startswith("Campo(s):"):

            self.indice_atual.campos = self.separar_campos(
                self.valor_linha(linha)
            )

            self.indice_atual = None

            return

    # =====================================================

    def novo_relacionamento(self, linha):

        self.relacionamento_atual = Relacionamento(
            nome=self.valor_linha(linha)
        )

        self.tabela_atual.adicionar_relacionamento(
            self.relacionamento_atual
        )

        self.campo_atual = None
        self.indice_atual = None

    # =====================================================

    def processar_relacionamento(self, linha):

        if linha.startswith("Tabela referenciada:"):

            self.relacionamento_atual.tabela_destino = (
                self.valor_linha(linha)
            )

            return

        if linha.startswith("Campo(s) na origem:"):

            self.relacionamento_atual.origem = (
                self.separar_campos(
                    self.valor_linha(linha)
                )
            )

            return

        if linha.startswith("Campo(s) no destino:"):

            self.relacionamento_atual.destino = (
                self.separar_campos(
                    self.valor_linha(linha)
                )
            )

            self.relacionamento_atual = None

            return


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    ARQUIVO = Path(
        r"C:\Repositorios\agent-sql\docs\Arquivo TBS\Comercial.txt"
    )

    parser = Parser(ARQUIVO)

    tabelas = parser.parse()

    PASTA_SAIDA = Path(
    r"C:\Repositorios\agent-sql\docs\tabelas\Comercial"
    )

    gerador = MarkdownGenerator(PASTA_SAIDA)

    gerador.gerar_todos(tabelas)

    print("Arquivos Markdown gerados com sucesso!")
    print(f"\nTotal de tabelas: {len(tabelas)}\n")

    for tabela in tabelas[:5]:

        print("=" * 80)
        print(f"TABELA: {tabela.nome}")
        print(f"DESCRIÇÃO: {tabela.descricao}")
        print("=" * 80)

        print("\nCAMPOS")

        for campo in tabela.campos:

            print(
                f"{campo.nome:15}"
                f"{campo.tipo:20}"
                f"{'SIM' if campo.nulo else 'NÃO':6}"
                f"{campo.descricao}"
            )

        print("\nCHAVE PRIMÁRIA")
        print(tabela.chave_primaria)

        print("\nÍNDICES")

        for indice in tabela.indices:

            print(f"Nome   : {indice.nome}")
            print(f"Tipo   : {indice.tipo}")
            print(f"Campos : {indice.campos}")
            print()

        print("\nRELACIONAMENTOS")

        for rel in tabela.relacionamentos:

            print(f"Nome    : {rel.nome}")
            print(f"Tabela  : {rel.tabela_destino}")
            print(f"Origem  : {rel.origem}")
            print(f"Destino : {rel.destino}")
            print()