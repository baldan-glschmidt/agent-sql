# R161EMP

## Descrição

Bs - Solicitação Empréstimo

---

## Resumo

- Campos: 36
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CmpEmp | Date | Não | Data Empréstimo |
| CodMtv | Number(003,0) | Sim | Código Motivo |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento |
| RgrEve | Number(003,0) | Sim | Regra Específica do Evento |
| VlrJur | Number(013,4) | Sim | Valor Juros |
| VlrEmp | Number(011,2) | Sim | Valor Empréstimo |
| VlrPar | Number(011,2) | Sim | Valor Parcela |
| VlrFut | Number(011,2) | Sim | Valor Futuro |
| CheSer | String(001) | Sim | Checou Serasa |
| DatCre | Date | Sim | Data Crédito |
| DatLib | Date | Sim | Data Liberação |
| DatPag | Date | Sim | Data Pagamento 1 Parcela |
| CodSen | String(040) | Sim | Senha |
| NroEmp | String(030) | Sim | Número Empréstimo |
| NroPar | Number(003,0) | Sim | Número de Parcelas |
| NumChe | Number(004,0) | Sim | Código da Empresa |
| TipChe | Number(001,0) | Sim | Tipo Colaborador |
| CadChe | Number(009,0) | Sim | Cadastro do Chefe |
| NumSub | Number(004,0) | Sim | Código da Empresa |
| TipSub | Number(001,0) | Sim | Tipo Colaborador |
| CadSub | Number(009,0) | Sim | Cadastro do Subchefe |
| ApoChe | String(001) | Sim | Aprovação Chefe |
| ObsEmp | String(500) | Sim | Observação |
| AteCri | String(001) | Sim | Atende os Critérios Definidos |
| SitChe | String(001) | Sim | Situação Aprov. Chefe |
| SitSub | String(001) | Sim | Situação Aprov. Subchefe |
| SitApo | Number(002,0) | Sim | Situação |
| ObsApo | String(500) | Sim | Observação Sobre Aprovação |
| CodMoa | Number(003,0) | Sim | Código Motivo Aprovação |
| DatOrd | Date | Sim | Data Pagamento Colaborador |
| DatAte | Date | Sim | Data Atendimento |
| HorAte | Number(005,0) | Sim | Hora Atendimento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161EMP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R161EMP_004

**Tabela:** R161MOT

| Origem | Destino |
|--------|---------|
| CodMtv | CodMtv |

### IR_R161EMP_006

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

