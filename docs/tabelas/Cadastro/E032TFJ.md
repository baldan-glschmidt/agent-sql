# E032TFJ

## Descrição

Cadastros - Financeiras - Juros por Parcelas de Financiamento

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFin | Number(004,0) | Não | Código da financeira |
| QtdPar | Number(002,0) | Não | Quantidade de parcelas do financiamento |
| NumTab | Number(008,0) | Não | Número da tabela de financiamento para exportação |
| JrsMin | Number(005,2) | Sim | Valor de juros mínimo para financiamento |
| JrsMax | Number(005,2) | Sim | Valor de juros máximo para financiamento |
| PerJrs | Number(005,2) | Sim | Percentual de juros para financiamento |
| VlrCoe | Number(006,5) | Sim | Valor do coeficiente para financiamento |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFin
- NumTab
- QtdPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
