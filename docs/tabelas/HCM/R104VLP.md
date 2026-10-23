# R104VLP

## Descrição

Valores da Ação

---

## Resumo

- Campos: 6
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodPrc | Number(007,0) | Sim | Código da Ação |
| CodVal | Number(002,0) | Sim | Código do Valor |
| ValPgt | Number(011,2) | Sim | Valor |
| DatPgt | Date | Sim | Data do Pagamento |
| CodOem | Number(008,0) | Sim | Empresa que efetuo o pagamento |

---

## Chave Primária

Não possui.

---

## Índices

### R104VLPIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- CodPrc
- CodVal

---

## Relacionamentos

### IR_R104VLP_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104VLP_002

**Tabela:** R104VAL

| Origem | Destino |
|--------|---------|
| CodVal | CodVal |

