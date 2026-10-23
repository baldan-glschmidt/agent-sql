# R171MED

## Descrição

Professores - Médias

---

## Resumo

- Campos: 15
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
| CodCal | Number(005,0) | Não | Código de Cálculo |
| SeqMed | Number(005,0) | Não | Sequência da Atividade |
| CmpMed | Date | Sim | Competência |
| CodApf | Number(004,0) | Sim | Código da Atividade |
| HorMes | Number(010,0) | Sim | Horas Mensais p/ Fechamento na Folha |
| DSRMes | Number(010,0) | Sim | DSR Mês |
| HorNot | Number(010,0) | Sim | Horas Mês Noturna do Professor |
| DSRNot | Number(010,0) | Sim | DSR Mês Noturna |
| EstSal | Number(004,0) | Sim | Código da Estrutura Salarial |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| ValHor | Number(011,2) | Sim | Valor Hora |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- SeqMed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R171MED_006

**Tabela:** R171ATI

| Origem | Destino |
|--------|---------|
| CodApf | CodApf |

