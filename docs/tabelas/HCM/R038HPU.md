# R038HPU

## Descrição

Histórico Servidor Público

---

## Resumo

- Campos: 21
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
| DatAlt | Date | Não | Data Alteração do Servidor Público |
| SitPub | Number(002,0) | Sim | Situação Pública |
| ObsSpu | String(050) | Sim | Observação Situação Pública |
| NatCar | Number(001,0) | Sim | Natureza do Cargo |
| ObsNCa | String(050) | Sim | Observação Natureza do Cargo |
| RegPre | Number(002,0) | Sim | Regime Previdenciário |
| ObsRPr | String(050) | Sim | Observação Regime Previdenciário |
| RegJur | Number(001,0) | Sim | Regime Jurídico |
| ObsRJu | String(050) | Sim | Observação Regime Jurídico |
| AtoPes | Number(002,0) | Sim | Ato Pessoal |
| RegTra | Number(001,0) | Sim | Regime Trabalho |
| VinPub | Number(002,0) | Sim | Vínculo Público |
| TipReg | Number(001,0) | Sim | Tipo de regime trabalhista |
| PanSeg | Number(001,0) | Sim | Tipo de plano de segregação da massa |
| RemCar | Number(001,0) | Sim | Indicar se o servidor optou pela remuneração do cargo efetivo |
| TetRgp | String(001) | Sim | Indicar se o servidor está sujeito ao teto do RGPS |
| IndAbo | String(001) | Sim | Indicar se o servidor recebe abono permanência |
| DatAbo | Date | Sim | Data de início do abono de permanência |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
