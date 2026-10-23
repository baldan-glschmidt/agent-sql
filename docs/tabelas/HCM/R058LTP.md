# R058LTP

## Descrição

Lista de Templates

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipLtp | Number(001,0) | Não | Tipo de Lista de Template |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| NumCra | Number(012,0) | Não | Número do Crachá da Lista |
| DatInc | Date | Sim | Data da Inclusão na Lista |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Inseriu na Lista |

---

## Chave Primária

- TipLtp
- CodRlg
- CodPlt
- NumCra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R058LTP_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R058LTP_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

