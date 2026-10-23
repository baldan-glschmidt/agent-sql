# R146BAS

## Descrição

Provisão - Bases

---

## Resumo

- Campos: 11
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| MesAno | Date | Não | Competência Provisões |
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| SeqPrv | Number(001,0) | Não | Sequência Para Saldo Transferido |
| TipVal | Number(002,0) | Não | Tipo de Valor |
| CodTab | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| ValEve | Number(010,2) | Sim | Valor do Evento na Base da Provisão |
| RegAju | Number(003,0) | Sim | Código da Regra de Ajuste da Base |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno
- TipPrv
- SeqPrv
- TipVal
- CodTab
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146BAS_004

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

### IR_R146BAS_006

**Tabela:** R146PRV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| MesAno | MesAno |
| TipPrv | TipPrv |
| SeqPrv | SeqPrv |
| TipVal | TipVal |

### IR_R146BAS_008

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

