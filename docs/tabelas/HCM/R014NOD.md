# R014NOD

## Descrição

Salários Normativos Diferenciados

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| CmpNor | Date | Não | Competência dos Salários Normativos Diferenciados |
| SeqNor | Number(003,0) | Não | Sequência |
| SalNor | Number(011,2) | Sim | Sal.Normativo Diferenciado |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| TipSal | Number(001,0) | Sim | Tipo de Salário |
| SinIda | String(001) | Sim | Sinal da Idade |
| NroIda | Number(002,0) | Sim | Número de Anos |
| SinSer | String(001) | Sim | Sinal Tempo Serviço |
| NroSer | Number(002,0) | Sim | Meses de Serviço |

---

## Chave Primária

- CodSin
- CmpNor
- SeqNor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014NOD_001

**Tabela:** R014NOR

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |
| CmpNor | CmpNor |

