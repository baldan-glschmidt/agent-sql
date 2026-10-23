# R017EPC

## Descrição

Estrutura de Postos de Trabalho - Histórico de Estrutura de Cargos

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| DatAlt | Date | Não | Data da Alteração da Estrutura de Organograma |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |

---

## Chave Primária

- EstPos
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017EPC_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R017EPC_002

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

