# R058HNF

## Descrição

Coletores Histórico Números Fiscais

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| DatAlt | Date | Não | Data Inicial |
| HorAlt | Number(005,0) | Não | Hora Inicial |
| DatFim | Date | Sim | Data Final |
| HorFim | Number(005,0) | Sim | Hora Final |
| NumFis | String(017) | Sim | Número Fiscal |

---

## Chave Primária

- CodPlt
- CodRlg
- DatAlt
- HorAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058HNF_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058HNF_001

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

