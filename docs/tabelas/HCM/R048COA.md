# R048COA

## Descrição

Contabilização com Contas Auxiliares

---

## Resumo

- Campos: 21
- Chave Primária: 16 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodLot | Number(009,0) | Não | Código Lote Contábil |
| DatLct | Date | Não | Data do Lançamento |
| CtaDeb | Number(008,0) | Não | Número Reduzido da Conta de Débito |
| CtaCre | Number(008,0) | Não | Número Reduzido da Conta de Crédito |
| ConFin | Number(007,0) | Não | Conta Financeira |
| ConDeb | String(030) | Não | Código da conta contábil |
| ConCre | String(030) | Não | Código da conta contábil |
| CenCus | String(030) | Não | Código do Centro de Custo |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código Lançamento Contábil |
| CodAux | Number(008,0) | Não | Código da Conta Auxiliar da Conta Contábil Reduzida |
| VlrLct | Number(011,2) | Sim | Vlr Lançamento |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| CplHis | String(100) | Sim | Complemento do Histórico Padrão |
| OriReg | Number(002,0) | Sim | Origem do Registro |
| OpcCtb | Number(001,0) | Sim | Opção da Contabilização |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- CodFil
- CodLot
- DatLct
- CtaDeb
- CtaCre
- ConFin
- ConDeb
- ConCre
- CenCus
- TabEve
- CodClc
- CodAux

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R048COA_003

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

