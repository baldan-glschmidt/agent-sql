# R047NAT

## Descrição

Dados da Integração por Empresa - Natureza de Despesa

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NatDes | Number(003,0) | Não | Código da Natureza de Despesa |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |

---

## Chave Primária

- CodCif
- NumEmp
- NatDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047NAT_001

**Tabela:** R047EMP

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |
| NumEmp | NumEmp |

