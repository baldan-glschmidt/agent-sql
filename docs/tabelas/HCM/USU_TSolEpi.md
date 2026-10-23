# USU_TSolEpi

## Descrição

Solicitação de EPIs

---

## Resumo

- Campos: 23
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_CodRqu | Number(009,0) | Não | Código da Requisição |
| USU_NumEmp | Number(004,0) | Não | Código da Empresa |
| USU_TipCol | Number(001,0) | Não | Tipo de Colaborador |
| USU_NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| USU_CodEpi | Number(008,0) | Não | Código do Epi |
| USU_DatSol | Date | Não | Data da Solicitação |
| USU_QtdEnt | Number(003,0) | Não | Quantidade Solicitada |
| USU_DatDev | Date | Sim | Data da Devolução |
| USU_QtdDan | Number(003,0) | Sim | Quantidade Devolvida e Danificada |
| USU_SitSol | String(001) | Sim | Situação da Solicitação |
| USU_UsuApr | Number(010,0) | Sim | Usuário da aprovação |
| USU_DatApr | Date | Sim | Data da aprovação |
| USU_HorApr | Number(005,0) | Sim | Hora Aprovação |
| USU_CodCcu | String(018) | Não | Código Centro Custo Contábil |
| USU_MotSol | Number(001,0) | Sim | Motivo da Solicitação |
| USU_IniEmp | Date | Sim | Inicio Empréstimo |
| USU_FimEmp | Date | Sim | Fim Empréstimo |
| USU_MedEpi | String(003) | Sim | Medida do Epi |
| USU_MotRep | String(100) | Sim | Motivo Reprova |
| USU_SeqSol | Number(004,0) | Não | Sequência |
| USU_UsuSol | Number(010,0) | Sim | Código Usuário Solicitante |
| USU_ObsEmp | String(240) | Sim | Observação |
| USU_EntRot | String(001) | Sim | Enviar EPI pela Rota |

---

## Chave Primária

- USU_CodRqu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
