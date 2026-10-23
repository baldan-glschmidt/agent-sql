# R017RIS

## Descrição

Postos de Trabalho - Revisão descrição - Atividades de risco

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatHis | Date | Não | Data da revisão da descrição do Posto |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodAtv | Number(007,0) | Não | Código da Atividade |

---

## Chave Primária

- EstPos
- PosTra
- DatHis
- NumEmp
- CodAtv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017RIS_002

**Tabela:** R017HDE

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |
| DatHis | DatHis |

