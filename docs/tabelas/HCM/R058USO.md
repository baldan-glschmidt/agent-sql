# R058USO

## Descrição

Uso das Marcações Realizadas no Coletor

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| CodFnc | Number(002,0) | Não | Código da Função |
| UsoMar | Number(002,0) | Sim | Uso da Marcação Realizada no Relógio |

---

## Chave Primária

- CodPlt
- CodRlg
- CodFnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058USO_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058USO_001

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

