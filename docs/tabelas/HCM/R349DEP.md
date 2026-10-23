# R349DEP

## Descrição

S-5002 - eSocial - Identificação dos dependentes

---

## Resumo

- Campos: 14
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqDep | Number(009,0) | Não | Sequência |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| DepIrr | String(001) | Sim | Informar se é dependente para fins de dedução do IRRF |
| DatNas | Date | Sim | Data de nascimento do dependente |
| NomDep | String(070) | Sim | Nome do Dependente |
| TipDep | Number(002,0) | Sim | Tipo de Dependente eSocial |
| DesDep | String(100) | Sim | Descrição da dependência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqDep

---

## Índices

### R349DEPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
