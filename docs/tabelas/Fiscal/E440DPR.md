# E440DPR

## Descrição

Compras - Nota Fiscal de Entrada - Documento Fiscal Produtor Rural

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqDpr | Number(003,0) | Não | Sequência do documento fiscal do produtor rural |
| UfsDpr | String(002) | Sim | Sigla do estado do emitente do documento fiscal produtor rural |
| DatDpr | Date | Não | Data de emissão do documento fiscal produtor rural |
| ForDpr | Number(009,0) | Não | Código do fornecedor do documento fiscal produtor rural |
| CodEdc | String(003) | Sim | Espécie de documento para fins fiscais |
| SnfDpr | String(003) | Sim | Código da série do documento fiscal produtor rural |
| NumDpr | Number(009,0) | Sim | Número do documento fiscal produtor rural |
| ChvNfp | String(050) | Sim | Chave da Nota Fiscal do Produtor Eletrônica |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqDpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DPR_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440DPR_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

### IR_E440DPR_008

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| ForDpr | CodFor |

