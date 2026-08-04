# models.py

from dataclasses import dataclass, field


@dataclass
class Campo:
    nome: str = ""
    tipo: str = ""
    nulo: bool = True
    descricao: str = ""

    def __str__(self):
        return self.nome


@dataclass
class Indice:
    nome: str = ""
    tipo: str = ""
    campos: list[str] = field(default_factory=list)

    def __str__(self):
        return self.nome


@dataclass
class Relacionamento:
    nome: str = ""
    tabela_destino: str = ""
    origem: list[str] = field(default_factory=list)
    destino: list[str] = field(default_factory=list)

    def __str__(self):
        return f"{self.nome} -> {self.tabela_destino}"


@dataclass
class Tabela:
    nome: str = ""
    descricao: str = ""

    campos: list[Campo] = field(default_factory=list)

    chave_primaria: list[str] = field(default_factory=list)

    indices: list[Indice] = field(default_factory=list)

    relacionamentos: list[Relacionamento] = field(default_factory=list)

    @property
    def total_campos(self) -> int:
        return len(self.campos)

    @property
    def total_indices(self) -> int:
        return len(self.indices)

    @property
    def total_relacionamentos(self) -> int:
        return len(self.relacionamentos)

    def adicionar_campo(self, campo: Campo):
        self.campos.append(campo)

    def adicionar_indice(self, indice: Indice):
        self.indices.append(indice)

    def adicionar_relacionamento(self, relacionamento: Relacionamento):
        self.relacionamentos.append(relacionamento)

    def __str__(self):
        return (
            f"Tabela({self.nome}) | "
            f"Campos={self.total_campos} | "
            f"PK={len(self.chave_primaria)} | "
            f"Índices={self.total_indices} | "
            f"Relacionamentos={self.total_relacionamentos}"
        )