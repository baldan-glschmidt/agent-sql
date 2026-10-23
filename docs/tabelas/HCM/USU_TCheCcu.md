# USU_TCheCcu

## Descrição

Tabela de Chefias por Centro de Custo para relatorio Ronda

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_NumEmp | Number(004,0) | Não | Codigo Empresa |
| USU_CodCcu | String(018) | Não | Codigo Centro Custo |
| USU_NomRes | String(040) | Sim | Nome Responsavel |
| USU_AdmInd | String(010) | Sim | Administrac?o/Industria |
| USU_NumCadRes | Number(009,0) | Sim | RE Responsável Gerente |
| USU_TipCol | Number(001,0) | Sim | Tipo Colaborador |
| USU_CadResSup | Number(009,0) | Sim | RE Responsável Supervisor |
| USU_CadResCo | Number(009,0) | Sim | RE Responsável Coordenador |

---

## Chave Primária

- USU_NumEmp
- USU_CodCcu

---

## Índices

### USU_CheCcu

**Tipo:** Não unico

Campos:
- USU_NumEmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
