# R353EXS

## Descrição

eSocial - perAnt - Detalhamento das deduções com exigibilidade suspensa

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| CodRec | Number(006,0) | Não | Código de receita do IRRF sobre rendimentos do trabalho |
| SeqJcr | Number(009,0) | Não | Sequência |
| SeqVpj | Number(009,0) | Não | Sequência |
| SeqExs | Number(009,0) | Não | Sequência |
| TipDed | Number(001,0) | Sim | Indicativo do tipo de dedução |
| VlrDed | Number(014,2) | Sim | Dedução da base de cálculo do IR com exigibilidade suspensa |
| CnpjEn | Number(014,0) | Sim | Número de inscrição da entidade de previdência complementar |
| CfjIns | String(014) | Sim | Número de inscrição da entidade de previdência complementar |
| VlrPat | Number(014,2) | Sim | Contribuição do ente público à Funpresp (Previdência Complementar do Servidor) |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CodRec
- SeqJcr
- SeqVpj
- SeqExs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
