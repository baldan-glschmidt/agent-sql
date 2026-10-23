# R350DNC

## Descrição

S-1210 - eSocial - Dependentes não enviados S-2200/S-2205/S-2300/S-2400/S-2405

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqDnc | Number(009,0) | Não | Sequência |
| CpfDep | Number(011,0) | Sim | Número de inscrição no CPF |
| DatNas | Date | Sim | Data de Nascimento |
| NomDep | String(070) | Sim | Nome do Dependente |
| DepIRF | String(001) | Sim | Dependente do trabalhador para fins de dedução de seu rendimento tributável pelo Imposto de Renda |
| TipDep | Number(002,0) | Sim | Tipo de Dependente |
| DesDep | String(100) | Sim | Descrição da Dependência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqDnc

---

## Índices

### R350DNCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
