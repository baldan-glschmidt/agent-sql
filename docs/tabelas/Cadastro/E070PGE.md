# E070PGE

## Descrição

Cadastros - Empresas - Parâmetros Gerais

---

## Resumo

- Campos: 2
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| EmpMod | String(001) | Sim | Indica se a empresa somente serve como modelo para duplicação de empresa |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E070PGE_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

