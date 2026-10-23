# R068CNR

## Descrição

Consumo Refeição

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodRef | Number(003,0) | Não | Código da Refeição |
| CodPlt | Number(005,0) | Não | Código do Site |
| RlgCon | Number(005,0) | Não | Código do Coletor no Consumo |
| FncCon | Number(002,0) | Não | Código da Função no Consumo |

---

## Chave Primária

- NumEmp
- CodRef
- CodPlt
- RlgCon
- FncCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R068CNR_001

**Tabela:** R068TRF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodRef | CodRef |

### IR_R068CNR_002

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

