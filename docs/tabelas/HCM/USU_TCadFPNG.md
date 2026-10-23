# USU_TCadFPNG

## Descrição

Cadastro de férias pagas e não gozadas

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| USU_NumEmp | Number(004,0) | Não | Código da Empresa |
| USU_TipCol | Number(001,0) | Não | Tipo de Colaborador |
| USU_NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| USU_DatAlt | Date | Não | Data Alteração |
| USU_IniFer | Date | Sim | Inicio Férias (Aquisitivo) |
| USU_FimFer | Date | Sim | Fim Férias (Aquisitivo) |
| USU_SitCre | Number(003,0) | Não | Situação Crédito |
| USU_DiaSal | Number(003,0) | Sim | Dias Saldo |
| USU_NumCra | Number(012,0) | Não | Número do Crachá |
| USU_IntAlm | Time | Sim | Intervalo Almoço |
| USU_SitFPNG | String(001) | Sim | Situação FPNG |
| USU_SitDeb | Number(003,0) | Não | Situação Débito |
| USU_IniDes | Date | Não | Inicio Descanso |
| USU_FimDes | Date | Não | Fim Descanso |

---

## Chave Primária

- USU_NumEmp
- USU_TipCol
- USU_NumCad
- USU_DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
