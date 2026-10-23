# R096MED

## Descrição

Medida do Epi

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodEpi | Number(008,0) | Não | Código do Epi |
| MedEpi | String(006) | Sim | Medida do Epi |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodEpi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R096MED_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R096MED_003

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

