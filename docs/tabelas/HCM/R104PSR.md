# R104PSR

## Descrição

JR - Autor - Cenário

---

## Resumo

- Campos: 14
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| DatCen | Date | Não | Data do cenário |
| SeqCen | Number(002,0) | Não | Sequência do cenário |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| VlrCal | Number(011,2) | Sim | Valor da empresa calculado |
| VlrCor | Number(011,2) | Sim | Valor da empresa corrigido |
| VlrCol | Number(011,2) | Sim | Valor do colaborador |
| VlrCoC | Number(011,2) | Sim | Valor do colaborador corrigido |
| IdeCal | String(001) | Sim | Identifica se o cenário foi calculado |
| DatCal | Date | Sim | Data do último cálculo |
| DatCor | Date | Sim | Data da última correção |

---

## Chave Primária

- NumEmp
- CodPrc
- DatCen
- SeqCen
- EmpAut
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104PSR_003

**Tabela:** R104PDC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |
| DatCen | DatCen |
| SeqCen | SeqCen |

