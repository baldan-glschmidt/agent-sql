from pathlib import Path
from models import Tabela, Campo, Indice, Relacionamento


ARQUIVO = Path(
    r"C:\Repositorios\agent-sql\docs\tabelas\Estoque.txt"
)


def valor_linha(linha: str) -> str:
    """
    Retorna tudo que estiver depois do primeiro ':'.
    """
    if ":" not in linha:
        return ""

    return linha.split(":", 1)[1].strip()


def separar_campos(valor: str) -> list[str]:
    """
    Converte:
        CodEmp;CodOri;NumOrp

    para:
        ["CodEmp", "CodOri", "NumOrp"]
    """
    if not valor:
        return []

    return [
        campo.strip()
        for campo in valor.split(";")
        if campo.strip()
    ]


def parse_arquivo(caminho: Path) -> list[Tabela]:

    tabelas: list[Tabela] = []

    tabela_atual = None
    campo_atual = None
    indice_atual = None
    relacionamento_atual = None

    aguardando_descricao_tabela = False

    with open(caminho, encoding="utf-8") as arquivo:

        for linha_original in arquivo:

            linha = linha_original.strip()

            if not linha:
                continue

            # ==========================================================
            # TABELA
            # ==========================================================

            if linha.startswith("Tabela:"):

                nome = valor_linha(linha)

                tabela_atual = Tabela(nome=nome)

                tabelas.append(tabela_atual)

                campo_atual = None
                indice_atual = None
                relacionamento_atual = None

                aguardando_descricao_tabela = True

                continue

            if tabela_atual is None:
                continue

            # ==========================================================
            # DESCRIÇÃO DA TABELA
            # ==========================================================

            if aguardando_descricao_tabela:

                if linha.startswith("Descr"):

                    tabela_atual.descricao = valor_linha(linha)

                    aguardando_descricao_tabela = False

                continue

            # ==========================================================
            # NOVO CAMPO
            # ==========================================================

            if linha.startswith("Nome do Campo:"):

                campo_atual = Campo(
                    nome=valor_linha(linha)
                )

                tabela_atual.campos.append(campo_atual)

                indice_atual = None
                relacionamento_atual = None

                continue

            # ==========================================================
            # DADOS DO CAMPO
            # ==========================================================

            if campo_atual is not None:

                if linha.startswith("Tipo do Campo:"):

                    campo_atual.tipo = valor_linha(linha)

                    continue

                if linha.startswith("Permite Nulo:"):

                    valor = valor_linha(linha).lower()

                    # O arquivo está trazendo:
                    # "N o" em vez de "Não"
                    campo_atual.nulo = not valor.startswith("n")

                    continue

                if linha.startswith("Descr"):

                    campo_atual.descricao = valor_linha(linha)

                    continue

            # ==========================================================
            # CHAVE PRIMÁRIA
            # ==========================================================

            if linha.startswith("Nome da Chave prim"):

                # A partir daqui não estamos mais lendo campo.
                campo_atual = None

                continue

            if linha.startswith("Campos da Chave prim"):

                tabela_atual.chave_primaria = separar_campos(
                    valor_linha(linha)
                )

                campo_atual = None

                continue

            # ==========================================================
            # ÍNDICE
            # ==========================================================

            if linha.startswith("Nome do") and "ndice:" in linha:

                campo_atual = None
                relacionamento_atual = None

                indice_atual = Indice(
                    nome=valor_linha(linha)
                )

                tabela_atual.indices.append(indice_atual)

                continue

            if indice_atual is not None:

                if linha.startswith("Tipo do") and "ndice:" in linha:

                    indice_atual.tipo = valor_linha(linha)

                    continue

                if linha.startswith("Campo(s):"):

                    indice_atual.campos = separar_campos(
                        valor_linha(linha)
                    )

                    continue

            # ==========================================================
            # RELACIONAMENTO
            # ==========================================================

            if linha.startswith("Relacionamento:"):

                campo_atual = None
                indice_atual = None

                relacionamento_atual = Relacionamento(
                    nome=valor_linha(linha)
                )

                tabela_atual.relacionamentos.append(
                    relacionamento_atual
                )

                continue

            if relacionamento_atual is not None:

                if linha.startswith("Tabela referenciada:"):

                    relacionamento_atual.tabela_destino = (
                        valor_linha(linha)
                    )

                    continue

                if linha.startswith("Campo(s) na origem:"):

                    relacionamento_atual.origem = separar_campos(
                        valor_linha(linha)
                    )

                    continue

                if linha.startswith("Campo(s) no destino:"):

                    relacionamento_atual.destino = separar_campos(
                        valor_linha(linha)
                    )

                    continue

    return tabelas


# ==============================================================
# EXECUÇÃO
# ==============================================================

if __name__ == "__main__":

    tabelas = parse_arquivo(ARQUIVO)

    print("=" * 80)
    print(f"TOTAL DE TABELAS: {len(tabelas)}")
    print("=" * 80)

    # Apenas as 10 primeiras tabelas
    for tabela in tabelas[:10]:

        print()
        print("=" * 80)
        print(f"TABELA : {tabela.nome}")
        print(f"DESCRIÇÃO : {tabela.descricao}")
        print("=" * 80)

        print(f"Quantidade de Campos: {len(tabela.campos)}")
        print()

        print("CAMPOS")
        print("-" * 80)

        for campo in tabela.campos:

            print(
                f"{campo.nome:15}"
                f"{campo.tipo:20}"
                f"{'SIM' if campo.nulo else 'NÃO':6}"
                f"{campo.descricao}"
            )

        print()

        print("CHAVE PRIMÁRIA")
        print("-" * 80)
        print(tabela.chave_primaria)

        print()

        print("ÍNDICES")
        print("-" * 80)

        for indice in tabela.indices:
            print(f"{indice.nome}")
            print(f"Tipo   : {indice.tipo}")
            print(f"Campos : {indice.campos}")
            print()

        print("RELACIONAMENTOS")
        print("-" * 80)

        for rel in tabela.relacionamentos:

            print(f"{rel.nome}")

            print(f"Tabela : {rel.tabela_destino}")
            print(f"Origem : {rel.origem}")
            print(f"Destino: {rel.destino}")

            print()