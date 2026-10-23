# R034ANU

## Descrição

Anuidades do Empregado

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| NumAnu | Number(002,0) | Não | Número de anos da anuidade |
| DatAnu | Date | Sim | Data Anuidade |
| TipAnu | String(001) | Sim | Tipo Anuidade |
| PerAnu | Number(005,2) | Sim | Percentual da anuidade |
| ValAnu | Number(011,2) | Sim | Valor da Anuidade |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- NumAnu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034ANU_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

