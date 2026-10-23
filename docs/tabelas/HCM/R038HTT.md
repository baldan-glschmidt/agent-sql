# R038HTT

## Descrição

Histórico de Teletrabalho

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
| DatIni | Date | Não | Data de Início de Teletrabalho |
| DatTer | Date | Sim | Data de Término de Teletrabalho |
| QtdHor | Number(005,0) | Sim | Quantidade de horas de antecedência para solicitação de comparecimento |
| CusCom | Number(001,0) | Sim | Responsável pelo custo do comparecimento |
| RepLid | String(050) | Sim | Periodicidade na qual o colaborador deve reportar ao líder |
| ValAju | Number(013,4) | Sim | Valor da ajuda de custo |
| DetAju | String(500) | Sim | Detalhamento da ajuda de custo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
