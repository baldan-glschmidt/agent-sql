# R161LEE

## Descrição

Bs - Levantamento S.E. Eventos

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatIni | Date | Não | Data Inicial do Atendimento |
| HorIni | Number(005,0) | Não | Hora Inicial do Atendimento |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CmpEve | Date | Não | Competência de Eventos |
| VlrEve | Number(011,2) | Sim | Valor Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni
- TabEve
- CodEve
- CmpEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161LEE_004

**Tabela:** R161ATE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| HorIni | HorIni |

### IR_R161LEE_006

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

