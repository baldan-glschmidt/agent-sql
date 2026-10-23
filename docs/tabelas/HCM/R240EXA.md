# R240EXA

## Descrição

Analytics SeniorX - Exames/ASO

---

## Resumo

- Campos: 13
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
| CodExa | Number(004,0) | Não | Código Exame |
| DatSol | Date | Não | Data Solicitação do Exame |
| DatExa | Date | Sim | Data da Realização do Exame |
| DatPro | Date | Sim | Data da Próxima Realização do Exame |
| DatVal | Date | Sim | Data da Validade do Exame |
| CodAte | Number(006,0) | Sim | Código Atendente |
| NumAte | Number(009,0) | Sim | Número do Atestado Médico |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última geração |
| DthAlt | Number(014,6) | Sim | Data/Hora em que foi realizada a última geração |
| CodFic | Number(009,0) | Sim | Código Ficha Médica |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodExa
- DatSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R240EXA_003

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

