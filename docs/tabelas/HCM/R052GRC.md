# R052GRC

## Descrição

GRCS - Guia Recolhimento Contribuição Sindical

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| ComGrc | Date | Não | Competência GRCS |
| TipGrc | Number(002,0) | Não | Tipo da GRCS |
| CodCtr | Number(009,0) | Não | Código Contrib.(Filial/Terc. e Colab.) |
| CodSin | Number(004,0) | Não | Código do Sindicato |
| VlrCap | Number(011,2) | Sim | Capital Social Empresa    C33 |
| TotEmp | Number(011,2) | Sim | Total Empresa             C34 |
| TotEst | Number(011,2) | Sim | Total Estabelecimento     C35 |
| CapEst | Number(011,2) | Sim | Capital Estabelecimento   C36 |
| BasCtr | Number(011,2) | Sim | Base Cálc. Contribuição   C37 |
| QtdCtr | Number(005,0) | Sim | Qtd.Empregados Contrib.   C38 |
| TotRem | Number(011,2) | Sim | Total da Remuneração      C39 |
| QemEst | Number(005,0) | Sim | Qtd.Empregados Estabelec. C40 |
| QemNao | Number(005,0) | Sim | Nro. Empregados Não Contribuem (41) |
| ValCtr | Number(011,2) | Sim | Valor da Contribuição (C42) |
| OriCtr | String(001) | Sim | Origem Contribuição |
| DatRec | Date | Sim | Data de Recolhimento |
| EncInc | Number(014,2) | Sim | Encargos Incidentes |

---

## Chave Primária

- NumEmp
- ComGrc
- TipGrc
- CodCtr
- CodSin

---

## Índices

### R052GRCIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- CodSin
- ComGrc
- TipGrc
- CodCtr

---

## Relacionamentos

### IR_R052GRC_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R052GRC_004

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

