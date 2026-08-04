# E032TPC

## Descrição

Cadastros - Financeiras - Financiamento Definido por Parcelas e Dias de Carência

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFin | Number(004,0) | Não | Código da financeira |
| QtdPar | Number(002,0) | Não | Quantidade de parcelas do financiamento |
| DiaCar | Number(003,0) | Não | Quantidade de dias de carência para pagamento da 1ª parcela |
| NumTab | Number(008,0) | Não | Número da tabela de financiamento para exportação |
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
- DiaCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
