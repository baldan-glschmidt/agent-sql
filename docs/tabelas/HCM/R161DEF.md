# R161DEF

## Descrição

Bs - Definições Empréstimos

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Codigo da Empresa |
| CmpDef | Date | Não | Competência das Definições |
| RgrLev | Number(003,0) | Sim | Código do Levantamento Sócio-Econômico |
| AbrRen | String(100) | Sim | Abrangência de Eventos para Renda |
| AbrDes | String(100) | Sim | Abrangência de Eventos para Desconto |
| MesCar | Number(002,0) | Sim | Meses de Carência |
| VlrAvu | Number(002,0) | Sim | Valor |
| DiaEmp | String(001) | Sim | Dia Desconto Parcela |
| CalJur | String(001) | Sim | Tipo de Cálculo dos Juros |
| IndJur | Number(003,0) | Sim | Tabela de Índice de Juros |
| DiaInd | Number(002,0) | Sim | Dia de Aplicação do Índice |
| PerInt | String(001) | Sim | Período utilizado para a integração das parcelas |

---

## Chave Primária

- NumEmp
- CmpDef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
