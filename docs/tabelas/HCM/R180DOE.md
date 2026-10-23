# R180DOE

## Descrição

Def. Contas p/ Outra Empresa

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodOem | Number(008,0) | Não | Código Outra Empresa |
| FilCtb | Number(006,0) | Sim | Filial Contábil |

---

## Chave Primária

- NumEmp
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R180DOE_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R180DOE_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

