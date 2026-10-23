# R068VDR

## Descrição

Valores Diferenciados Refeição

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodRef | Number(003,0) | Não | Código da Refeição com Valor Diferenciado |
| TipDia | Number(001,0) | Não | Tipo de Dia dos Valores Diferenciados |
| DatIni | Date | Não | Data Inicial Valor Diferenciado da Refeição |
| DatFim | Date | Sim | Data Final Valor Diferenciado da Refeição |
| ValNor | Number(013,4) | Sim | Valor Normal da Refeição |
| ValSeg | Number(013,4) | Sim | Valor da Segunda Refeição no Dia |
| ValTer | Number(013,4) | Sim | Valor da Terceira Refeição no Dia |
| ValDem | Number(013,4) | Sim | Valor das Demais Refeição no Dia |
| ValSCo | Number(013,4) | Sim | Valor sem o Consumo da Refeição |
| ValSRe | Number(013,4) | Sim | Valor sem a Reserva da Refeição |
| ValREm | Number(013,4) | Sim | Valor da Refeição para a Empresa |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodRef
- TipDia
- DatIni

---

## Índices

### R068VDRIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatIni
- DatFim

---

## Relacionamentos

### IR_R068VDR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

