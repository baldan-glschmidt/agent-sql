# E140IPO

## Descrição

Vendas - Notas Fiscais de Saída - Itens de Produto - Ordens de Compra Vinculadas

---

## Resumo

- Campos: 14
- Chave Primária: 0 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Sim | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| DatEnt | Date | Sim | Data da entrada |
| SeqEnt | Number(006,0) | Sim | Sequência de entrada  na data |
| SeqPro | Number(006,0) | Sim | Sequência de produto na data |
| FilNfv | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| FilOcp | Number(005,0) | Não | Código da filial |
| NumOcp | Number(008,0) | Não | Número da ordem de compra |
| SeqIpo | Number(004,0) | Não | Sequência de item da ordem de compra |
| QtdDev | Number(014,5) | Não | Quantidade devolvida do item da nota fiscal de saída |

---

## Chave Primária

Não possui.

---

## Índices

### E140IPOIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- FilNfv
- CodSnf
- NumNfv
- SeqIpv
- FilOcp
- NumOcp
- SeqIpo

### E140IPOIndice2

**Tipo:** Não unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
