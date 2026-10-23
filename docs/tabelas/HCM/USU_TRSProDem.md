# USU_TRSProDem

## Descrição

Análise Processo de Demissão

---

## Resumo

- Campos: 18
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_CodRqu | Number(009,0) | Não | Código Requisição |
| USU_DatRef | Date | Não | Data de Referência de Inserção das Análises |
| USU_NumEmp | Number(004,0) | Não | Código da Empresa do Colaborador Substituído |
| USU_TipCol | Number(001,0) | Não | Tipo Colabolador Substituído |
| USU_NumCad | Number(009,0) | Não | Cadastro do Colaborador Substituído |
| USU_EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos do Colaborador Substituído |
| USU_CodCar | String(024) | Sim | Código do Cargo do Colaborador Substituído |
| USU_CodCcu | String(018) | Sim | Código do Centro de Custo do Colaborador Substituído |
| USU_SitAna | String(001) | Sim | Situação da Análise Realizada |
| USU_DatAna | Date | Sim | Data da Realização da Análise |
| USU_MotAna | String(3000) | Sim | Motivo da Análise Realizada |
| USU_DatExa | Date | Sim | Data da Realização da Etapa do Exame Médico |
| USU_ParExa | String(001) | Sim | Parecer do Exame Médico |
| USU_PrvAdm | Date | Sim | Data de Previsão de Admissão |
| USU_DatInt | Date | Sim | Data de Integração |
| USU_DatDem | Date | Sim | Data de Demissão |
| USU_Status | String(030) | Sim | Status da Proposta de Demissão |
| USU_SitPrc | String(001) | Sim | Situação do Processo de Demissão |

---

## Chave Primária

- USU_CodRqu
- USU_DatRef

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
