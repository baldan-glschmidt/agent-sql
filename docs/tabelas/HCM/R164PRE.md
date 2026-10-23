# R164PRE

## Descrição

BS - Preços Plano

---

## Resumo

- Campos: 29
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOem | Number(008,0) | Não | Código da Seguradora |
| CodPla | Number(003,0) | Não | Código Plano |
| PerRef | Date | Não | Competência do Valores |
| FaiSal | Number(011,2) | Não | Faixa Salarial Teto |
| TipSeg | String(001) | Sim | Tipo da Informação |
| TotTit | Number(010,4) | Sim | Total do Titular |
| SubTit | Number(011,5) | Sim | Subsidiado do Titular |
| TotDpl | Number(010,4) | Sim | Total do Dependente Legal |
| SubDpl | Number(011,5) | Sim | Subsidiado do Dependente Legal |
| TotOut | Number(010,4) | Sim | Total dos Outros Dependentes |
| SubOut | Number(010,4) | Sim | Subsidiado dos Outros Dependentes |
| TetCol | Number(011,2) | Sim | Teto Internação Colaborador |
| TetDep | Number(011,2) | Sim | Teto Internação Dependente |
| VlrIns | Number(011,2) | Sim | Valor Inscrição |
| VlrMen | Number(011,2) | Sim | Valor Mensalidade |
| SegVia | Number(011,2) | Sim | Valor Segunda Via |
| VlrChe | Number(011,2) | Sim | Valor C.H. |
| TetDes | Number(011,2) | Sim | Teto Desconto |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| EveIns | Number(004,0) | Sim | Evento Inscrição |
| RgrIns | Number(003,0) | Sim | Regra do Evento Inscrição |
| EveMen | Number(004,0) | Sim | Evento Mensalidade |
| RgrMen | Number(003,0) | Sim | Regra do Evento Mensalidade |
| EveSeg | Number(004,0) | Sim | Evento Segunda Via |
| RgrSeg | Number(003,0) | Sim | Regra Segunda Via |
| EveChe | Number(004,0) | Sim | Evento C.H. |
| RgrChe | Number(003,0) | Sim | Regra do Evento C.H. |
| EveSer | Number(004,0) | Sim | Evento Serviços |
| RgrSer | Number(003,0) | Sim | Regra do Evento Serviço |

---

## Chave Primária

- CodOem
- CodPla
- PerRef
- FaiSal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R164PRE_001

**Tabela:** R164PLA

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |
| CodPla | CodPla |

