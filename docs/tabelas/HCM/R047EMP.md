# R047EMP

## Descrição

Dados da Integração por Empresa

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCif | Number(003,0) | Não | Código de Integração Financeira |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTrs | String(005) | Sim | Código da Transação |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |
| CodNtg | Number(004,0) | Sim | Nat. Gasto |
| GruCon | String(003) | Sim | Código do grupo de contas a receber ou pagar |
| CcuPad | String(018) | Sim | Código Centro Custo Padrão |

---

## Chave Primária

- CodCif
- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R047EMP_000

**Tabela:** R047CIF

| Origem | Destino |
|--------|---------|
| CodCif | CodCif |

### IR_R047EMP_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

