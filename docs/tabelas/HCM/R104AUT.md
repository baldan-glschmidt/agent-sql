# R104AUT

## Descrição

JR - Autor(Pessoa Jurídica)

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| CodOem | Number(008,0) | Não | Código do Autor - código da empresa na tabela  outra empresa |

---

## Chave Primária

- NumEmp
- CodPrc
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104AUT_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104AUT_002

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

