# R030POS

## Descrição

Empresa - Histórico de Estruturas de Postos

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatAlt | Date | Não | Data da Alteração da Estrutura de Postos |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosDef | String(024) | Sim | Posto de Trabalho padrão para criar os históricos dos Colaboradores sem Posto |

---

## Chave Primária

- NumEmp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030POS_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R030POS_002

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R030POS_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosDef | PosTra |

