# R020PRJ

## Descrição

Rateios - Projetos

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRat | Number(009,0) | Não | Código do Rateio |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodPrj | Number(008,0) | Sim | Código do Projeto |
| CodFas | Number(004,0) | Sim | Código da Fase do Projeto |

---

## Chave Primária

- CodRat
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020PRJ_000

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

