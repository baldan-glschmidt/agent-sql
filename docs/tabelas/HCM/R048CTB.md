# R048CTB

## Descrição

Contabilização - Nova

---

## Resumo

- Campos: 46
- Chave Primária: 0 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colabolador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CodFil | Number(006,0) | Sim | Código da Filial |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |
| SeqPag | Number(010,0) | Sim | Sequência de Pagamento |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Sim | Código Lançamento Contábil |
| DatLan | Date | Sim | Data do Lançamento |
| OpcCtb | Number(002,0) | Sim | Opção da Contabilização |
| CodCal | Number(005,0) | Sim | Código de Cálculo |
| CodLot | Number(009,0) | Sim | Código do Lote Contábil |
| SeqLot | Number(009,0) | Sim | Sequência do Lote |
| DebCre | String(001) | Sim | Tipo Lançamento |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| CplHis | String(100) | Sim | Complemento do Histórico Padrão |
| NatDes | Number(003,0) | Sim | Natureza de Despesa do Lançamento Contábil |
| ConFin | Number(007,0) | Sim | Conta Financeira |
| CodAux | Number(008,0) | Sim | Código da Conta Auxiliar |
| ConGer | String(019) | Sim | Código da Conta Gerencial |
| PerRat | Number(005,2) | Sim | % Rateio |
| CodFor | Number(009,0) | Sim | Código do Fornecedor |
| ClcPDb | Number(004,0) | Sim | CLC de contrapartida - Partidas dobradas |
| NumDoc | String(025) | Sim | Número do Documento |
| NomCon | String(100) | Sim | Nome da conta |
| OriCtb | String(001) | Sim | Origem da informação |
| LotSAP | Number(006,0) | Sim | Lote Contábil Paginação |
| ValLan | Number(014,2) | Sim | Valor do Lançamento Contábil |
| FilCtb | Number(006,0) | Sim | Filial Contábil |
| CcuRat | String(018) | Sim | Centro de Custo (Rateio) |
| LocRat | Number(009,0) | Sim | Local do Organograma (Rateio) |
| CodRat | Number(009,0) | Sim | Código do Rateio |
| ConDeb | String(030) | Sim | Código da Conta Contábil de Débito |
| ConCre | String(030) | Sim | Código da Conta Contábil de Crédito |
| RedDeb | Number(008,0) | Sim | Número da Conta Reduzida de Débito |
| RedCre | Number(008,0) | Sim | Número da Conta Reduzida de Crédito |
| FilCtP | Number(006,0) | Sim | Filial Contábil (Padrão) |
| CodCcu | String(018) | Sim | Centro de Custo (Padrão) |
| NumLoc | Number(009,0) | Sim | Local do Organograma (Padrão) |
| RatPad | Number(009,0) | Sim | Código do Rateio (Padrão) |
| ConDeP | String(030) | Sim | Código da Conta Contábil de Débito (Padrão) |
| ConCrP | String(030) | Sim | Código da Conta Contábil de Crédito (Padrão) |
| RedDeP | Number(008,0) | Sim | Número da Conta Reduzida de Débito (Padrão) |
| RedCrP | Number(008,0) | Sim | Número da Conta Reduzida de Crédito (Padrão) |
| DefCon | Number(001,0) | Sim | Definição Contas Contábeis |

---

## Chave Primária

Não possui.

---

## Índices

### R048CTBIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- DatLan
- CodLot

### R048CTBIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodOem
- TabEve
- CodClc
- DatLan
- OpcCtb
- CodCcu
- TabOrg
- NumLoc
- CodRat
- FilCtb
- ConGer
- SeqPag
- CodFil

---

## Relacionamentos

Nenhum relacionamento cadastrado.
