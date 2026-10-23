# R085PSP

## Descrição

Param Orç-Salários não tabelados por posto

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Posto de Trabalho |
| CmpPrm | Date | Não | Competência |
| ValSal | Number(011,2) | Sim | Salário a ser considerado no aumento/redução do quadro |
| ValSim | Number(011,2) | Sim | Sal.simulado a ser considerado no aumento/redução do quadro |

---

## Chave Primária

- NumEmp
- CodCen
- CmpPrm
- EstPos
- PosTra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R085PSP_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

