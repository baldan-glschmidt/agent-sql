# E014CCC

## Descrição

Tabelas - Características de Clientes/Fornecedores - Componentes

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCcl | String(003) | Não | Código da característica de cliente/fornecedor |
| CodCcc | Number(003,0) | Não | Código do componente da característica de cliente/fornecedor |
| DesCcc | String(030) | Não | Descrição do componente da característica de cliente/fornecedor |
| AbrCcc | String(010) | Sim | Abreviatura do componente da característica de cliente/fornecedor |

---

## Chave Primária

- CodCcl
- CodCcc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E014CCC_000

**Tabela:** E014CCL

| Origem | Destino |
|--------|---------|
| CodCcl | CodCcl |

