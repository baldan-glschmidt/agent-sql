# R348EXT

## Descrição

eSocial - Conferência IRRF - Pagamentos Residente Fiscal no Exterior

---

## Resumo

- Campos: 20
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| DatPag | Date | Não | Data de pagamento |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipOri | Number(002,0) | Não | Tipo de origem do pagamento do IRRF |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| IndNif | Number(001,0) | Sim | Indicativo do número de identificação fiscal |
| NifExt | String(030) | Sim | Número de identificação fiscal no exterior |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| BaiLog | String(090) | Sim | Nome do bairro/distrito |
| CidLog | String(050) | Sim | Nome da cidade |
| EstExt | String(040) | Sim | Nome da província/estado |
| PosLog | String(012) | Sim | Código de endereçamento postal - estrangeiro |
| TelExt | String(015) | Sim | Número do telefone |
| CodPai | Number(003,0) | Sim | Código do país |
| ForTri | Number(002,0) | Sim | Forma de tributação |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- DatPag
- TipCol
- NumCad
- TipOri
- CodCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
