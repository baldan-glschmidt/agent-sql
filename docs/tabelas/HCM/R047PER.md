# R047PER

## Descrição

Pendências Integração Financeira - Rateio

---

## Resumo

- Campos: 38
- Chave Primária: 11 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DhiPen | Number(014,6) | Não | Data/Hora Inclusão da Pendência |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| TipTit | String(003) | Não | Tipo de Título |
| CodFor | Number(009,0) | Não | Código Fornecedor |
| CodRat | Number(009,0) | Sim | Código do Rateio |
| CodCcu | String(018) | Não | Código Centro Custo |
| CodPrj | Number(008,0) | Não | Código do Projeto |
| CodFas | Number(004,0) | Não | Código da Fase do Projeto |
| CodRed | Number(008,0) | Não | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Não | Conta Financeira |
| TipTis | String(003) | Sim | Tipo de Título do ERP |
| CodCif | Number(003,0) | Sim | Código de Integração Financeira |
| CodTrs | String(005) | Sim | Código da Transação |
| SerNfi | String(003) | Sim | Série da Nota Fiscal ERP |
| VncTit | Date | Sim | Vencimento do Título |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CodCal | Number(005,0) | Sim | Código de Cálculo |
| IniPer | Date | Sim | Data Início do Período |
| IniFer | Date | Sim | Data Início das Férias |
| DatDem | Date | Sim | Data da Demissão |
| CodDep | Number(003,0) | Sim | Código do dependente |
| CodSin | Number(004,0) | Sim | Código do sindicato |
| RatGps | Number(009,0) | Sim | Código do Rateio |
| StsOpr | String(001) | Sim | Operação - Inclusão / Exclusão |
| TipAgr | String(001) | Sim | Tipo de Agrupamento |
| CodNtg | Number(004,0) | Sim | Nat. Gasto |
| ValRat | Number(015,2) | Sim | Valor Rateado do Titulo |
| NumTit | String(030) | Sim | Número do Título |
| OriGps | Number(002,0) | Sim | Código de Origem |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| DatEnt | Date | Sim | Data de Entrada do Título |
| DatEmi | Date | Sim | Data de Emissão do Título |
| ModPag | String(001) | Sim | Agrupar Modo de Pagamento do Salário |
| FilSap | Number(006,0) | Sim | Filial ERP |
| TipCif | Number(001,0) | Não | Tipo de CIF INSS |
| CodUsu | Number(010,0) | Sim | Usuário |

---

## Chave Primária

- DhiPen
- NumEmp
- CodFil
- TipTit
- CodFor
- CodCcu
- CodPrj
- CodFas
- CodRed
- CtaFin
- TipCif

---

## Índices

### R047PERIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodCal

### R047PERIndice3

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodCal
- StsOpr
- CodCif

---

## Relacionamentos

Nenhum relacionamento cadastrado.
