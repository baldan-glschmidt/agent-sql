# R348CCD

## Descrição

eSocial - Conferência IRRF - Código de Receita por CPF - Diário

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| PerDia | Date | Não | Período apuração diário |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| CodRec | Number(006,0) | Não | Código de receita relativo ao IRRF sobre rendimentos do trabalho |
| DiaApu | Number(002,0) | Sim | Dia de Apuração - Período de apuração diário do Código de Receita |
| ForTri | Number(002,0) | Sim | Forma de tributação |
| CodPai | Number(003,0) | Sim | Código do país |
| ValPag | Number(014,2) | Sim | Valor pago a residente ou domiciliado no exterior |
| ValIrf | Number(014,2) | Sim | Valor IRRF sobre rendimentos do trabalho pagos a residente, para fins fiscais, no exterior |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- PerDia
- CpfTra
- CodRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
