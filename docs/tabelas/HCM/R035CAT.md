# R035CAT

## Descrição

PPP - CATs Registradas

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqReg | Number(004,0) | Não | Sequência do registro |
| DatCat | Date | Sim | Data de registro da  CAT |
| DatEmi | Date | Sim | Data da emissão da CAT |
| CATPPP | String(040) | Sim | Número da CAT - para constar no PPP |
| SitRPP | Number(001,0) | Sim | Situação do Registro |
| IgnReg | String(001) | Sim | Define se o registro será ignorado na emissão do PPP |
| IndCon | String(001) | Sim | Apresenta se o registro está em conflito com outro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
