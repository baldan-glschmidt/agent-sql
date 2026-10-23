# R096FIL

## Descrição

Epi - Fornecedores - Filiais

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
| CodEpi | Number(008,0) | Não | Código do Epi |
| CodOem | Number(008,0) | Não | Código do Fornecedor |
| EmpFil | Number(006,0) | Não | Empresa Filial |
| AbrFil | String(100) | Sim | Abrangência de Filial |

---

## Chave Primária

- CodEpi
- CodOem
- EmpFil

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096FIL_000

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

### IR_R096FIL_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

