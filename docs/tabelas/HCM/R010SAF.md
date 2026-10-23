# R010SAF

## Descrição

Fechamento Saldo de Situações do Colaborador

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodSal | Number(002,0) | Não | Código do Saldo |
| CmpSal | Date | Não | Competência do Fechamento do Saldo |
| SalAnt | Number(010,0) | Sim | Valor Anterior do Saldo (Competência Anterior) |
| DebMes | Number(010,0) | Sim | Valor de Débito no Mês |
| CreMes | Number(010,0) | Sim | Valor de Crédito no Mês |
| SalAtu | Number(010,0) | Sim | Valor Atual do Saldo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodSal
- CmpSal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010SAF_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R010SAF_003

**Tabela:** R010CSA

| Origem | Destino |
|--------|---------|
| CodSal | CodSal |

