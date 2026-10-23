# R017HCV

## Descrição

Postos de Trabalho - Histórico do controle de vagas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da Estrutura de Postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de trabalho |
| DatAlt | Date | Não | Define a data de alteração do histórico de controle de vagas do posto |
| TipCva | Number(001,0) | Sim | Define como será feito o controle de vagas para este posto de trabalho |
| PosAgr | String(024) | Sim | Código do posto de trabalho agrupador |

---

## Chave Primária

- EstPos
- PosTra
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017HCV_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

