# E440DEC

## Descrição

Tabelas - Notas Fiscais de Entrada - Notas de Débito e Crédito

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| FinNfe | Number(001,0) | Sim | Tipo Finalidade da NF-e |
| NfeDeb | Number(002,0) | Sim | Tipo de Nota de Débito |
| NfeCre | Number(002,0) | Sim | Tipo de Nota de Crédito |
| ImAnRt | String(001) | Sim | Indicativo se a nota fiscal de crédito/débito deve ser integrada para tributos |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DEC_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440DEC_003

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

