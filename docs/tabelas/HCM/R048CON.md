# R048CON

## Descrição

Contabilização

---

## Resumo

- Campos: 19
- Chave Primária: 15 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
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
| VlrLct | Number(014,2) | Sim | Vlr Lançamento |
| HisPad | Number(004,0) | Não | Código Histórico Padrão |
| CplHis | String(100) | Sim | Complemento do Histórico Padrão |
| OpcCtb | Number(001,0) | Não | Opção da Contabilização |
| CodFor | Number(009,0) | Sim | Código Fornecedor |
| FilSap | Number(006,0) | Sim | Filial ERP |

---

## Chave Primária

- NumEmp
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
- HisPad
- OpcCtb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R048CON_001

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

