# R064PAR

## Descrição

Paradas

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Colaborador |
| DatIni | Date | Não | Data Inicial |
| HorIni | Number(005,0) | Não | Hora Inicial |
| QtdHPa | Number(010,0) | Sim | Quantidade de Horas Paradas de Trabalho |
| CodMPa | Number(006,0) | Sim | Código Motivo |
| QtdEPa | Number(010,0) | Sim | Quantidade de Horas Extras de Parada. |
| MotEpa | Number(006,0) | Sim | Código Motivo das Horas de Trabalho da Parada. |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064PAR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

