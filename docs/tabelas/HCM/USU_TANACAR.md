# USU_TANACAR

## Descrição

Análise de Propostas de Cargos e Salários

---

## Resumo

- Campos: 28
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_NumEmp | Number(004,0) | Não | Código da Empresa |
| USU_TipCol | Number(001,0) | Não | Tipo Colabolador |
| USU_NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| USU_DatRef | Date | Não | Data de Referência da Análise |
| USU_EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos Atual |
| USU_CodCar | String(024) | Sim | Código do Cargo Atual |
| USU_TipSal | Number(001,0) | Sim | Tipo do Salário Atual |
| USU_ValSal | Number(013,4) | Sim | Salário Atual |
| USU_ClaSal | String(005) | Sim | Classe Salarial Atual |
| USU_NivSal | String(005) | Sim | Nível Salarial Atual |
| USU_DatAdm | Date | Sim | Data de Admissão |
| USU_CodCcu | String(018) | Sim | Código do Centro de Custo Proposto do Colaborador |
| USU_EstPos | Number(003,0) | Não | Código da Estrutura de Postos de Trabalho Proposto |
| USU_PosTra | String(024) | Sim | Código do Posto de Trabalho Proposto |
| USU_EstCarPro | Number(004,0) | Sim | Código da Estrutura de Cargos Proposto |
| USU_CodCarPro | String(024) | Sim | Código do Cargo Proposto |
| USU_TipSalPro | Number(001,0) | Sim | Tipo do Salário Proposto |
| USU_ValSalPro | Number(013,4) | Sim | Salário Proposto |
| USU_ClaSalPro | String(005) | Sim | Classe Salarial Proposto |
| USU_NivSalPro | String(005) | Sim | Nível Salarial Proposto |
| USU_PerReaPro | Number(008,5) | Sim | % Reajuste Salário Proposto |
| USU_ComAno | String(3000) | Sim | Anotações Análise Realizada |
| USU_SitAna | String(001) | Sim | Aprovação  Análise |
| USU_DatApr | Date | Sim | Data de Aprovação da Proposta |
| USU_DatRep | Date | Sim | Data de Reprovação da Proposta |
| USU_SitWkf | Number(001,0) | Sim | Situação WorkFlow |
| USU_Status | String(030) | Sim | Status da Proposta de Aprovação de Cargos e Salários |
| USU_CcuAtu | String(018) | Sim | Código do Centro de Custo Atual do Colaborador |

---

## Chave Primária

- USU_NumEmp
- USU_TipCol
- USU_NumCad
- USU_DatRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
