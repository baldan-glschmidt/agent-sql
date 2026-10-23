# R020INT

## Descrição

Rateio - Integração

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRat | Number(009,0) | Não | Código do Rateio |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| CtaFin | Number(007,0) | Sim | Código da Conta Financeira |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |

---

## Chave Primária

- CodRat
- NumEmp
- CodCif

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R020INT_000

**Tabela:** R020RAT

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |

### IR_R020INT_001

**Tabela:** R020PRJ

| Origem | Destino |
|--------|---------|
| CodRat | CodRat |
| NumEmp | NumEmp |

