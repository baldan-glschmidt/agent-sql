# R047PEN

## Descrição

Pendências Integração Financeira

---

## Resumo

- Campos: 44
- Chave Primária: 5 campo(s)
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
| TipTis | String(003) | Sim | Tipo de Título do ERP |
| CodCif | Number(003,0) | Sim | Código de Integração Financeira |
| CodTrs | String(005) | Sim | Código da Transação |
| SerNfi | String(003) | Sim | Série da Nota Fiscal ERP |
| VncTit | Date | Sim | Vencimento do Título |
| ValTit | Number(015,2) | Sim | Valor do Título |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CodCal | Number(005,0) | Sim | Código de Cálculo |
| TipCal | Number(002,0) | Sim | Tipo do Cálculo |
| IniPer | Date | Sim | Data Início do Período |
| IniFer | Date | Sim | Data Início das Férias |
| DatDem | Date | Sim | Data da Demissão |
| CodDep | Number(003,0) | Sim | Código do dependente |
| CodSin | Number(004,0) | Sim | Código do sindicato |
| RatGps | Number(009,0) | Sim | Código do Rateio |
| ObsTit | String(300) | Sim | Observação do Título |
| StsOpr | String(001) | Sim | Operação - Inclusão / Exclusão |
| TipAgr | String(001) | Sim | Tipo de Agrupamento |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |
| CodNtg | Number(004,0) | Sim | Nat. Gasto |
| CodCcu | String(018) | Sim | Código Centro Custo |
| CodRat | Number(009,0) | Sim | Código de Rateio do C.Custo |
| OriGps | Number(002,0) | Sim | Código de Origem |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| DatEnt | Date | Sim | Data de Entrada do Título |
| DatEmi | Date | Sim | Data de Emissão do Título |
| ModPag | String(001) | Sim | Agrupar Modo de Pagamento do Salário |
| FilSap | Number(006,0) | Sim | Filial ERP |
| GruCon | String(003) | Sim | Código do grupo de contas a receber ou pagar |
| CodRec | Number(004,0) | Sim | Código de Recolhimento - DARF |
| TitTer | Number(009,0) | Sim | Número do RPCI |
| CodUsu | Number(010,0) | Sim | Usuário |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| NumTit | String(030) | Sim | Número do Título |
| IdProc | String(100) | Sim | ID do Processo |
| TipOpe | Number(001,0) | Sim | Tipo de Operação |

---

## Chave Primária

- DhiPen
- NumEmp
- CodFil
- TipTit
- CodFor

---

## Índices

### R047PENIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodCal

### R047PENIndice3

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
