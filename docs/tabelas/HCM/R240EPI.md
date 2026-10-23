# R240EPI

## Descrição

Analytics SeniorX - EPIs

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodEpi | Number(008,0) | Não | Código do Epi |
| DatEnt | Date | Não | Data da Entrega |
| SeqDie | Number(003,0) | Não | Sequência da Distribuição |
| QtdEnt | Number(003,0) | Sim | Quantidade da Entrega |
| QtdDev | Number(003,0) | Sim | Quantidade da Devolução |
| QtdDan | Number(003,0) | Sim | Quantidade Devolvida e Danificada |
| DatVal | Date | Sim | Data da Validade |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última geração |
| DthAlt | Number(014,6) | Sim | Data/Hora em que foi realizada a última geração |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodEpi
- DatEnt
- SeqDie

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R240EPI_003

**Tabela:** R096EPI

| Origem | Destino |
|--------|---------|
| CodEpi | CodEpi |

