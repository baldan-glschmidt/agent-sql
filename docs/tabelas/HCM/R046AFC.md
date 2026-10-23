# R046AFC

## Descrição

Acumulados Ficha Financeira - p/ Cálculo

---

## Resumo

- Campos: 36
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| TotPro | Number(011,2) | Sim | Total de Proventos |
| TotVan | Number(011,2) | Sim | Total de Vantagens |
| TotDes | Number(011,2) | Sim | Total de Descontos |
| LiqFol | Number(011,2) | Sim | Valor Líquido da Folha |
| HorExt | Number(010,0) | Sim | Total de Horas Extras no Mês |
| AdiNot | Number(010,0) | Sim | Horas de Adicional Noturno no Mês |
| AdiIns | Number(010,0) | Sim | Horas de Insalubridade no Mês |
| AdiPer | Number(010,0) | Sim | Horas de Periculosidade no Mês |
| ValTro | Number(014,2) | Sim | Valor do Troco |
| TroAnt | Number(014,2) | Sim | Valor do Troco Anterior |
| ValEst | Number(014,2) | Sim | Valor do Estouro |
| EstAnt | Number(014,2) | Sim | Valor do Estouro Anterior |
| AcuV01 | Number(014,2) | Sim | Valor do Acumulador 1 |
| AcuV02 | Number(014,2) | Sim | Valor do Acumulador 2 |
| AcuV03 | Number(014,2) | Sim | Valor do Acumulador 3 |
| AcuV04 | Number(014,2) | Sim | Valor do Acumulador 4 |
| AcuV05 | Number(014,2) | Sim | Valor do Acumulador 5 |
| AcuV06 | Number(014,2) | Sim | Valor do Acumulador 6 |
| AcuV07 | Number(014,2) | Sim | Valor do Acumulador 7 |
| AcuV08 | Number(014,2) | Sim | Valor do Acumulador 8 |
| AcuV09 | Number(014,2) | Sim | Valor do Acumulador 9 |
| AcuV10 | Number(014,2) | Sim | Valor do Acumulador 10 |
| AcuV11 | Number(014,2) | Sim | Valor do Acumulador 11 |
| AcuV12 | Number(014,2) | Sim | Valor do Acumulador 12 |
| AcuV13 | Number(014,2) | Sim | Valor do Acumulador 13 |
| AcuV14 | Number(014,2) | Sim | Valor do Acumulador 14 |
| AcuV15 | Number(014,2) | Sim | Valor do Acumulador 15 |
| AcuV16 | Number(014,2) | Sim | Valor do Acumulador 16 |
| AcuV17 | Number(014,2) | Sim | Valor do Acumulador 17 |
| AcuV18 | Number(014,2) | Sim | Valor do Acumulador 18 |
| AcuV19 | Number(014,2) | Sim | Valor do Acumulador 19 |
| AcuV20 | Number(014,2) | Sim | Valor do Acumulador 20 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046AFC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R046AFC_003

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

