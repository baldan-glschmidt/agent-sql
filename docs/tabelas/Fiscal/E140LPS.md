# E140LPS

## Descrição

Vendas - Ligação Entre Itens de Produto e Itens de Serviço de Notas Fiscais de Saída

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item de produto na nota fiscal de saída |
| SeqLps | Number(004,0) | Não | Sequência de ligação |
| EmpRlc | Number(004,0) | Não | Empresa da Nota Fiscal Relacionada |
| FilRlc | Number(005,0) | Não | Filial da Nota Fiscal Relacionada |
| SnfRlc | String(003) | Não | Série da Nota Fiscal Relacionada |
| NfvRlc | Number(009,0) | Não | Número da nota fiscal de saída relacionada |
| IsvRlc | Number(003,0) | Não | Sequência do Item de Serviço Relacionado |
| ProSer | String(001) | Não | Indicativo se o registro foi gerado a partir do produto ou serviço |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- SeqLps

---

## Índices

### E140LPSIndice2

**Tipo:** Não unico

Campos:
- EmpRlc
- FilRlc
- SnfRlc
- NfvRlc
- IsvRlc

---

## Relacionamentos

### IR_E140LPS_004

**Tabela:** E140IPV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIpv | SeqIpv |

### IR_E140LPS_010

**Tabela:** E140ISV

| Origem | Destino |
|--------|---------|
| EmpRlc | CodEmp |
| FilRlc | CodFil |
| SnfRlc | CodSnf |
| NfvRlc | NumNfv |
| IsvRlc | SeqIsv |

