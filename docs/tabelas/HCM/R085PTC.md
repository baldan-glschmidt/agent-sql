# R085PTC

## Descrição

Param Orç-Salários não tabelados por C.Custo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CmpPer | Date | Não | Competência |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| ValSal | Number(011,2) | Sim | Salário a ser considerado no aumento e redução quadro |
| ValSim | Number(011,2) | Sim | Sal.simulado a ser considerado no aumento/redução quadro |

---

## Chave Primária

- NumEmp
- CodCen
- CmpPer
- CodCcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PTC_003

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

