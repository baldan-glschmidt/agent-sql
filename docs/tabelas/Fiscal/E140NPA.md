# E140NPA

## Descrição

Vendas - Nota Fiscal de Saída - Dados do Conhecimento de Transporte - Notas fiscais dos Documentos Anteriores

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| CodTra | Number(009,0) | Não | Código da Transportadora |
| SeqDoc | Number(004,0) | Não | Sequências dos documentos anteriores |
| SeqNpa | Number(004,0) | Não | Sequências das Notas fiscais de documentos anteriores |
| ChvDoe | String(050) | Sim | Chave do documento eletrônico |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- CodTra
- SeqDoc
- SeqNpa

---

## Índices

### E140NPAIndice1

**Tipo:** Não unico

Campos:
- CodTra

---

## Relacionamentos

### IR_E140NPA_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140NPA_003

**Tabela:** E140CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140NPA_004

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodTra | CodCli |

