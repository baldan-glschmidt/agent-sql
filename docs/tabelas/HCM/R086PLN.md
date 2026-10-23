# R086PLN

## Descrição

Plano de Ação do Acidente do Trabalho

---

## Resumo

- Campos: 6
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
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAct
- HorAct
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086PLN_004

**Tabela:** R086ACT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatAct | DatAct |
| HorAct | HorAct |

### IR_R086PLN_005

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

