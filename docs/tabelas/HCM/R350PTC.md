# R350PTC

## Descrição

S-2245 - eSocial - Profissionais responsáveis pelo treinamento/capacitação/exercício simulado (Obsoleto)

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqTre | Number(009,0) | Não | Sequência |
| SeqPtc | Number(009,0) | Não | Sequência |
| CpfPro | Number(011,0) | Sim | CPF do profissional responsável pelo treinamento/capacitação/exercício simulado |
| NomPro | String(070) | Sim | Nome do profissional responsável pelo treinamento/capacitação/exercício simulado |
| TipPro | Number(001,0) | Sim | Tipo do profissional que ministrou o treinamento/capacitação/exercício simulado |
| ForPro | String(255) | Sim | Formação do profissional responsável pelo treinamento/capacitação/exercício simulado |
| CodCBO | String(006) | Sim | CBO referente formação do profissional responsável pelo treinamento/capacitação/exercício simulado |
| IndNac | Number(001,0) | Sim | Indicativo de nacionalidade |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqTre
- SeqPtc

---

## Índices

### R350PTCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
