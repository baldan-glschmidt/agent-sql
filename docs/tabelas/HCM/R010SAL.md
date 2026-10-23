# R010SAL

## Descrição

Saldo de Situações do Colaborador

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
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
| DatAlt | Date | Não | Data da Alteração do Saldo |
| OriAlt | String(001) | Não | Origem da Alteração do Saldo |
| HorSal | Number(010,0) | Sim | Valor da Alteração do Saldo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodSal
- DatAlt
- OriAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010SAL_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R010SAL_003

**Tabela:** R010CSA

| Origem | Destino |
|--------|---------|
| CodSal | CodSal |

