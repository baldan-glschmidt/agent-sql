# R099ARN

## Descrição

Análise Ruído - NPS

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAna | Date | Não | Data da Análise |
| HorAna | Number(005,0) | Não | Hora da Análise |
| DatRef | Date | Sim | Data de Referência |
| IntMed | Number(004,1) | Sim | Integração da Média de 60 segundos |
| NPSMax | Number(004,1) | Sim | NPS Máximos |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAna
- HorAna

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R099ARN_003

**Tabela:** R099ARD

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatAna | DatAna |

