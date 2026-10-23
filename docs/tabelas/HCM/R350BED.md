# R350BED

## Descrição

S-2400 - eSocial - Dependentes do beneficiário

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqBen | Number(009,0) | Não | Sequência |
| SeqBed | Number(009,0) | Não | Sequência |
| TipDep | Number(002,0) | Sim | Tipo de Dependente eSocial |
| NomDep | String(070) | Sim | Nome do Dependente |
| DatNas | Date | Sim | Data de nascimento |
| CpfDep | Number(011,0) | Sim | Número de Inscrição no CPF |
| SexDep | String(001) | Sim | Sexo do Dependente |
| DepIRR | String(001) | Sim | Informar se é dependente para fins de dedução do IRRF |
| IncTra | String(001) | Sim | Informar se o dependente tem incapacidade física ou mental para o trabalho |
| CodDep | Number(002,0) | Sim | Código do dependente |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| DESDEP | String(100) | Sim | Descrição da dependência |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqBen
- SeqBed

---

## Índices

### R350BEDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
