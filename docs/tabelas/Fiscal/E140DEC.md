# E140DEC

## Descrição

Tabelas - Notas Fiscais de Saída - Notas de Débito e Crédito

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| FinNfe | Number(001,0) | Sim | Tipo Finalidade da NF-e |
| NfeDeb | Number(002,0) | Sim | Tipo de Nota de Débito |
| NfeCre | Number(002,0) | Sim | Tipo de Nota de Crédito |
| NumTit | String(015) | Sim | Número do título a receber |
| CodTpt | String(003) | Sim | Código do tipo de título a receber |
| SeqMov | Number(004,0) | Sim | Sequência de movimento do título |
| VlrMov | Number(015,2) | Sim | Valor do movimento do título |
| ImAnRt | String(001) | Sim | Indicativo se a nota fiscal de crédito/débito deve ser integrada para tributos |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140DEC_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140DEC_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

