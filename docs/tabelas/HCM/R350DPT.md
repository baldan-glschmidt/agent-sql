# R350DPT

## Descrição

S-2205 - eSocial - Alteração de Dados Cadastrais do Trabalhador - Dependentes

---

## Resumo

- Campos: 17
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
| SeqAda | Number(009,0) | Não | Sequência |
| SeqDpt | Number(009,0) | Não | Sequência |
| TipDep | Number(002,0) | Sim | Tipo de Dependente eSocial |
| NomDep | String(070) | Sim | Nome do Dependente |
| DatNas | Date | Sim | Data de nascimento dependente |
| CpfDep | Number(011,0) | Sim | Número de Inscrição no CPF do dependente |
| SexDep | String(001) | Sim | Sexo do Dependente |
| DepIrr | String(001) | Sim | Informar se é dependente para fins de dedução do IRRF |
| DepSaf | String(001) | Sim | Informar se é dependente para fins de recebimento do benefício |
| IncTra | String(001) | Sim | Informar se o dependente tem incapacidade física ou mental para o trabalho |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| CodDep | Number(002,0) | Sim | Código do dependente |
| DESDEP | String(100) | Sim | Descrição da dependência |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAda
- SeqDpt

---

## Índices

### R350DPTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
