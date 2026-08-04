# markdown.py

from pathlib import Path
from models import Tabela


class MarkdownGenerator:

    def __init__(self, pasta_saida: Path):
        self.pasta_saida = pasta_saida
        self.pasta_saida.mkdir(parents=True, exist_ok=True)

    def gerar(self, tabela: Tabela):

        arquivo = self.pasta_saida / f"{tabela.nome}.md"

        with open(arquivo, "w", encoding="utf-8") as md:

            # ==========================================================
            # Cabeçalho
            # ==========================================================

            md.write(f"# {tabela.nome}\n\n")

            md.write("## Descrição\n\n")
            md.write(f"{tabela.descricao}\n\n")

            md.write("---\n\n")

            # ==========================================================
            # Resumo
            # ==========================================================

            md.write("## Resumo\n\n")
            md.write(f"- Campos: {len(tabela.campos)}\n")
            md.write(f"- Chave Primária: {len(tabela.chave_primaria)} campo(s)\n")
            md.write(f"- Índices: {len(tabela.indices)}\n")
            md.write(f"- Relacionamentos: {len(tabela.relacionamentos)}\n\n")

            md.write("---\n\n")

            # ==========================================================
            # Campos
            # ==========================================================

            md.write("## Campos\n\n")

            md.write("| Campo | Tipo | Nulo | Descrição |\n")
            md.write("|--------|------|------|-----------|\n")

            for campo in tabela.campos:

                md.write(
                    f"| {campo.nome} | "
                    f"{campo.tipo} | "
                    f"{'Sim' if campo.nulo else 'Não'} | "
                    f"{campo.descricao} |\n"
                )

            md.write("\n---\n\n")

            # ==========================================================
            # Chave Primária
            # ==========================================================

            md.write("## Chave Primária\n\n")

            if tabela.chave_primaria:

                for campo in tabela.chave_primaria:
                    md.write(f"- {campo}\n")

            else:

                md.write("Não possui.\n")

            md.write("\n---\n\n")

            # ==========================================================
            # Índices
            # ==========================================================

            md.write("## Índices\n\n")

            if tabela.indices:

                for indice in tabela.indices:

                    md.write(f"### {indice.nome}\n\n")

                    md.write(f"**Tipo:** {indice.tipo}\n\n")

                    md.write("Campos:\n")

                    for campo in indice.campos:
                        md.write(f"- {campo}\n")

                    md.write("\n")

            else:

                md.write("Nenhum índice cadastrado.\n\n")

            md.write("---\n\n")

            # ==========================================================
            # Relacionamentos
            # ==========================================================

            md.write("## Relacionamentos\n\n")

            if tabela.relacionamentos:

                for rel in tabela.relacionamentos:

                    md.write(f"### {rel.nome}\n\n")

                    md.write(f"**Tabela:** {rel.tabela_destino}\n\n")

                    md.write("| Origem | Destino |\n")
                    md.write("|--------|---------|\n")

                    for origem, destino in zip(rel.origem, rel.destino):

                        md.write(
                            f"| {origem} | {destino} |\n"
                        )

                    md.write("\n")

            else:

                md.write("Nenhum relacionamento cadastrado.\n")

    def gerar_todos(self, tabelas: list[Tabela]):

        for tabela in tabelas:
            self.gerar(tabela)