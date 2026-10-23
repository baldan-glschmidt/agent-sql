# R353VPJ

## Descrição

eSocial - perAnt - Valores - não retenção de tributos ou a depósitos judiciais

---

## Resumo

- Campos: 13
- Chave Primária: 7 campo(s)
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
| InApVl | Number(001,0) | Sim | Indicativo de período de apuração |
| VlrNre | Number(014,2) | Sim | Valor da retenção não efetuada por processo administrativo ou judicial |
| VlrDep | Number(014,2) | Sim | Valor do depósito judicial em função de processo administrativo ou judicial |
| VlrAtu | Number(014,2) | Sim | Valor da compensação relativa ao ano calendário em função de processo judicial |
| VlrAnt | Number(014,2) | Sim | Valor da compensação relativa a anos anteriores em função de processo judicial |
| VlrSus | Number(014,2) | Sim | Valor do rendimento com exigibilidade suspensa |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CodRec
- SeqJcr
- SeqVpj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
