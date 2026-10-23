# R035RMB

## Descrição

PPP - Responsáveis pela Monitoração Biológica

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqReg | Number(004,0) | Não | Sequência do registro |
| DatIni | Date | Sim | Data de início da atuação do Responsável |
| DatTer | Date | Sim | Data de término da atuação do Responsável |
| NomFun | String(040) | Sim | Nome do Responsável |
| NumNIT | Number(011,0) | Sim | NIS do Responsável |
| RegCon | String(020) | Sim | Registro no Conselho Profissional |
| EstCon | String(002) | Sim | UF do Conselho Profissional |
| SitCon | String(001) | Sim | Situação do Registro no Conselho |
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
