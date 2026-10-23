# R348ADV

## Descrição

eSocial - Conferência IRRF - Identificação Advogados

---

## Resumo

- Campos: 13
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| DatPag | Date | Não | Data de pagamento |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipOri | Number(002,0) | Não | Tipo da origem do pagamento do IRRF |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| SeqAdv | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do advogado |
| NumIns | Number(014,0) | Sim | Número de inscrição do advogado |
| CfjIns | String(014) | Sim | Número de inscrição do advogado |
| VlrAdv | Number(014,2) | Sim | Valor da despesa com advogados |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- DatPag
- TipCol
- NumCad
- TipOri
- CodCal
- SeqAdv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
