# R353CCR

## Descrição

eSocial - perAnt - Informações relativas a planos de previdência complementar

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
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
| SeqPre | Number(009,0) | Não | Sequência |
| TipPre | Number(001,0) | Sim | Tipo de previdência complementar |
| CnpjEn | Number(014,0) | Sim | Número de inscrição da entidade de previdência complementar |
| CfjIns | String(014) | Sim | Número de inscrição da entidade de previdência complementar |
| VlrDed | Number(014,2) | Sim | Valor da dedução relativa à previdência complementar |
| VlrD13 | Number(014,2) | Sim | Valor da dedução do 13º Salário relativa à previdência complementar |
| VlrPat | Number(014,2) | Sim | Valor da contribuição do ente público patrocinador da Funpresp |
| VlrP13 | Number(014,2) | Sim | Valor da contribuição do 13º Salário do ente público patrocinador da Funpresp |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- CodRec
- SeqPre

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
