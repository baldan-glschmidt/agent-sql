# R058LIS

## Descrição

Listas do Coletor

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
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| TipLis | Number(002,0) | Não | Tipo de Lista do Coletor |
| LisInc | String(012) | Sim | Nome do Arquivo da Lista de Inclusão |
| LimCra | Number(006,0) | Sim | Limite de Crachás para Geração da Lista |

---

## Chave Primária

- CodPlt
- CodRlg
- TipLis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058LIS_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

