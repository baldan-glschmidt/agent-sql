# E140LNS

## Descrição

Vendas - Ligação Entre Itens de Serviço de Notas Fiscais de Saída

---

## Resumo

- Campos: 11
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
| SeqIsv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| SeqLns | Number(004,0) | Não | Sequência de ligação |
| EmpRlc | Number(004,0) | Não | Empresa da Nota Fiscal Relacionada |
| FilRlc | Number(005,0) | Não | Filial da Nota Fiscal Relacionada |
| SnfRlc | String(003) | Não | Série da Nota Fiscal Relacionada |
| NfvRlc | Number(009,0) | Não | Número da nota fiscal de saída Relacionada |
| IsvRlc | Number(003,0) | Não | Sequência do Item de Serviço Relacionado |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIsv
- SeqLns

---

## Índices

### E140LNSIndice1

**Tipo:** Não unico

Campos:
- EmpRlc
- FilRlc
- SnfRlc
- NfvRlc
- IsvRlc

---

## Relacionamentos

### IR_E140LNS_004

**Tabela:** E140ISV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIsv | SeqIsv |

### IR_E140LNS_010

**Tabela:** E140ISV

| Origem | Destino |
|--------|---------|
| EmpRlc | CodEmp |
| FilRlc | CodFil |
| SnfRlc | CodSnf |
| NfvRlc | NumNfv |
| IsvRlc | SeqIsv |

