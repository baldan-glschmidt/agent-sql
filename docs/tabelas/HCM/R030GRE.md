# R030GRE

## Descrição

Grupo de Empresas - Empresas

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGru | Number(003,0) | Não | Código do Grupo de Empresas |
| NumEmp | Number(004,0) | Não | Código da Empresa |

---

## Chave Primária

- CodGru
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030GRE_000

**Tabela:** R030GRU

| Origem | Destino |
|--------|---------|
| CodGru | CodGru |

### IR_R030GRE_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

