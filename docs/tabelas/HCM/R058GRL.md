# R058GRL

## Descrição

Coletores do Grupo

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGrr | Number(003,0) | Não | Código do Grupo de Relógios |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor da Permissão |
| CodDsp | Number(009,0) | Sim | Código do Dispositivo |

---

## Chave Primária

- CodGrr
- CodRlg
- CodPlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058GRL_000

**Tabela:** R058GRR

| Origem | Destino |
|--------|---------|
| CodGrr | CodGrr |

### IR_R058GRL_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058GRL_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

