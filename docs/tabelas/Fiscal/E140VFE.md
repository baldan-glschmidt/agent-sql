# E140VFE

## Descrição

Tabelas - Notas Fiscais de SaÃ­da - Valores de Financiamento Externo

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | CÃ³digo da sÃ©rie da nota fiscal de saÃ­da |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| TotVen | Number(015,2) | Sim | Valor total da venda com financiamento externo |
| VlrEnc | Number(015,2) | Sim | Valor total dos encargos da venda com financiamento externo |
| VlrSeg | Number(015,2) | Sim | Valor do seguro embutido no valor do financiamento externo |
| NumPfi | String(015) | Sim | NÃºmero da proposta da financeira que originou a venda |
| CodFin | Number(004,0) | Sim | CÃ³digo da financeira utilizada no financiamento externo |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

### E140VFEIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFin
- NumPfi

---

## Relacionamentos

### IR_E140VFE_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140VFE_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

