# R047HIS

## Descrição

Histórico de Títulos Integrados no ERP

---

## Resumo

- Campos: 37
- Chave Primária: 10 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| TipTit | String(003) | Não | Tipo de Título |
| TipTis | String(003) | Sim | Tipo de Título do ERP |
| CodFor | Number(009,0) | Não | Código Fornecedor |
| CodCif | Number(003,0) | Sim | Código de Integração Financeira |
| CodTrs | String(005) | Sim | Código da Transação |
| SerNfi | String(003) | Sim | Série da Nota Fiscal ERP |
| VncTit | Date | Sim | Vencimento do Título |
| ValTit | Number(015,2) | Sim | Valor do Título |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| IniPer | Date | Sim | Data Início do Período |
| IniFer | Date | Sim | Data Início das Férias |
| DatDem | Date | Sim | Data da Demissão |
| CodDep | Number(003,0) | Não | Código do dependente |
| CodSin | Number(004,0) | Sim | Código do sindicato |
| RatGps | Number(009,0) | Sim | Código do Rateio |
| ObsTit | String(300) | Sim | Observação do Título |
| NumTit | String(030) | Não | Número do Título |
| StsCan | String(001) | Sim | Status Cancelamento |
| OriGps | Number(002,0) | Sim | Código de Origem |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa |
| CtaFin | Number(007,0) | Sim | Conta Financeira |
| TipAgr | String(001) | Sim | Tipo de Agrupamento |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CodNtg | Number(004,0) | Sim | Nat. Gasto |
| CodCcu | String(018) | Sim | Código Centro Custo Contábil |
| DatEnt | Date | Sim | Data de Entrada do Título |
| DatEmi | Date | Sim | Data de Emissão do Título |
| ModPag | String(001) | Sim | Agrupar Modo de Pagamento do Salário |
| FilSap | Number(006,0) | Sim | Filial ERP |
| TipCif | Number(001,0) | Não | Tipo de CIF INSS |
| GruCon | String(003) | Sim | Código do grupo de contas a receber ou pagar |
| CodUsu | Number(010,0) | Sim | Usuário |
| DatAux | Date | Não | Data Auxiliar |

---

## Chave Primária

- NumEmp
- CodFil
- TipTit
- CodFor
- TipCol
- NumCad
- NumTit
- CodDep
- TipCif
- CodCal

---

## Índices

### R047HISIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodCal
- StsCan
- CodCif
- TipTit

---

## Relacionamentos

Nenhum relacionamento cadastrado.
