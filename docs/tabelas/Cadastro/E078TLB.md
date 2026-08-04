# E078TLB

## Descrição

Tabelas - Títulos dos Movimentos dos Lotes de Baixa

---

## Resumo

- Campos: 6
- Chave Primária: 0 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Sim | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| NumTit | String(015) | Sim | Número do título a pagar/receber |
| CodTpt | String(003) | Sim | Código de Tipo de Título |
| CodFor | Number(009,0) | Sim | Código do fornecedor do título a pagar |
| ChvLot | String(024) | Sim | Chave do lote de baixa |

---

## Chave Primária

Não possui.

---

## Índices

### E078TLBIndice1

**Tipo:** Não unico

Campos:
- ChvLot

### E078TLBIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumTit
- CodTpt
- CodFor
- ChvLot

---

## Relacionamentos

Nenhum relacionamento cadastrado.
