# E070PFO

## Descrição

Cadastros - Filiais - Períodos de fechamento por Origem

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodOri | String(003) | Não | Código de Origem do Produto |
| EstPdi | Date | Sim | Período inicial de validade para movimentações dos estoques |
| EstPdf | Date | Sim | Período final de validade para movimentações dos estoques |
| EstPai | Date | Sim | Período inicial anterior de validade para movimentações dos estoques |
| EstPaf | Date | Sim | Período final anterior de validade para movimentações dos estoques |
| UlpVm1 | Date | Sim | Último período de valorização para multimoeda 1 |
| UlpVm2 | Date | Sim | Último período de valorização para multimoeda 2 |
| PdiAte | Date | Sim | Período inicial de atualização de estoques |
| PdfAte | Date | Sim | Período final de atualização de estoques |

---

## Chave Primária

- CodEmp
- CodFil
- CodOri

---

## Índices

### E070PFOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodOri

---

## Relacionamentos

### IR_E070PFO_002

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

