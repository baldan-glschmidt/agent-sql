# R195SMI

## Descrição

Cenário - Salário Mínimo

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| PerRef | Date | Não | Competência referência salário mínimo |
| SalMin | Number(011,2) | Sim | Valor do salário mínimo |

---

## Chave Primária

- NumEmp
- CodCen
- PerRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195SMI_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

