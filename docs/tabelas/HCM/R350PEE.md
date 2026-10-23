# R350PEE

## Descrição

S-1210 - eSocial - Informações complementares relativas a pagamentos a residente fiscal no exterior

---

## Resumo

- Campos: 20
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqIpe | Number(009,0) | Não | Sequência |
| SeqPee | Number(009,0) | Não | Sequência |
| CodPai | Number(003,0) | Sim | Código do país |
| IndNif | Number(001,0) | Sim | Indicativo do Número de Identificação Fiscal |
| NifExt | String(030) | Sim | Número de Identificação Fiscal no Exterior |
| ForTri | Number(002,0) | Sim | Formas de Tributação para Rendimentos de Beneficiários no Exterior |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| BaiLog | String(090) | Sim | Nome do bairro/distrito |
| CidLog | String(050) | Sim | Nome da Cidade |
| PosLog | String(012) | Sim | Código de Endereçamento Postal - estrangeiro |
| EstExt | String(040) | Sim | Nome da província/estado |
| TelExt | String(015) | Sim | Número do Telefone |
| PidExc | String(050) | Sim | Identificador da execução da pendência |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqIpe
- SeqPee

---

## Índices

### R350PEEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
