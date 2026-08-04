# E140IMP

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produto - Impostos

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa da nota fiscal de saída |
| CodFil | Number(005,0) | Não | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item de produto da nota fiscal de saída |
| CodImp | String(003) | Não | Código do imposto |
| QtdBas | Number(014,5) | Não | Quantidade base para cálculo do imposto |
| UniMed | String(003) | Não | Código da unidade de medida utilizada na base de cálculo do imposto |
| VlrUpf | Number(019,10) | Sim | Valor da unidade padrão fiscal na data da transação |
| PerAli | Number(006,3) | Não | Percentual da Alíquota |
| TotImp | Number(015,2) | Sim | Valor total do imposto calculado |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- CodImp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140IMP_004

**Tabela:** E140IPV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIpv | SeqIpv |

