# USU_TConCol

## Descrição

Tabela para cadastro de Convênios Médicos de Colaboradores

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_NumEmp | Number(004,0) | Não | Código da Empresa |
| USU_TipCol | Number(001,0) | Não | Tipo Colaborador |
| USU_NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| USU_DatAlt | Date | Não | Data da Alteração do C.Custo |
| USU_PlaSau | String(001) | Não | Nome do Plano de Saúde |
| USU_CodPsa | String(007) | Sim | Código do Plano de Saúde |
| USU_MatPsa | Number(015,0) | Sim | Número da Matrícula no Plano Saúde |
| USU_ExcPsa | Date | Sim | Data de Exclusão no Plano de Saúde |

---

## Chave Primária

- USU_NumEmp
- USU_TipCol
- USU_NumCad
- USU_DatAlt
- USU_PlaSau

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
