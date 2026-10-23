# R008SAL

## Descrição

Saldo de Eventos do Colaborador

---

## Resumo

- Campos: 8
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
| CodCal | Number(005,0) | Não | Código de Cálculo |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodSal | Number(004,0) | Não | Código do Saldo |
| HorSal | Number(010,0) | Sim | Valor do Saldo |
| OriAlt | String(001) | Sim | Origem do Valor do Saldo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- CodSal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R008SAL_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R008SAL_005

**Tabela:** R008CSA

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodSal | CodSal |

