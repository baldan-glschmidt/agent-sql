# R046HCT

## Descrição

Informações holerite - eConsignado

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colabolador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| InsFin | Number(003,0) | Sim | Instituição financeira |
| NomIns | String(100) | Sim | Nome Instituição Financeira |
| NumCtr | String(050) | Sim | Número do contrato alfanumérico |
| ValOri | Number(011,2) | Sim | Valor Original da Parcela |
| ValDes | Number(011,2) | Sim | Valor Descontado |
| ValDif | Number(011,2) | Sim | Valor Diferença |
| CmpAu1 | Number(011,2) | Sim | Campo auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo auxiliar 2 |
| CmpAu3 | Date | Sim | Campo auxiliar 3 |
| CmpAu4 | Number(009,0) | Sim | Campo auxiliar 4 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCal
- TabEve
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
