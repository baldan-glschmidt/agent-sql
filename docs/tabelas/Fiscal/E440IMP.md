# E440IMP

## Descrição

Compras - Notas Fiscais de Entrada - Impostos por Produto nos itens de Nota Fiscal

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| CodImp | String(003) | Não | Código do imposto |
| QtdBas | Number(014,5) | Não | Quantidade base para cálculo do imposto |
| UniMed | String(003) | Não | Código da Unidade de Medida utilizada na base de cálculo |
| VlrUpf | Number(019,10) | Sim | Valor da Unidade Padrão Fiscal na data da transação |
| PerAli | Number(006,3) | Não | Percentual da Alíquota |
| TotImp | Number(015,2) | Não | Valor total de imposto calculado |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- CodImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440IMP_005

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

