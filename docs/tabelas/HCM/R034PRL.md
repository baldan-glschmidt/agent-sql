# R034PRL

## Descrição

Registro Preliminar de Trabalhador

---

## Resumo

- Campos: 26
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| DatAdm | Date | Não | Data de Inclusão |
| SeqPrl | Number(001,0) | Não | Sequência |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| CodFil | Number(006,0) | Sim | Código da Filial |
| NomFun | String(040) | Sim | Nome do Colaborador |
| AdmCol | Date | Não | Data de Admissão |
| CodVin | Number(002,0) | Sim | Tipo de Vínculo |
| CateSo | Number(004,0) | Sim | Código da categoria eSocial |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| TipEst | Number(001,0) | Sim | Tipo de Estrutura |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| ValSal | Number(013,4) | Sim | Salário Atual |
| DatNas | Date | Sim | Data de nascimento do trabalhador |
| DurCon | Number(004,0) | Sim | Duração do Contrato de Trabalho |
| ProCon | Number(004,0) | Sim | Prorrogação do Contrato de Trabalho |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador ligado a este Registro Preliminar |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| MatEso | String(030) | Sim | Matrícula eSocial |
| ObjDet | String(255) | Sim | Objetivo do término de contrato por prazo determinado |
| OriReg | Number(001,0) | Sim | Origem do registro |

---

## Chave Primária

- NumEmp
- CpfTra
- DatAdm
- SeqPrl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
