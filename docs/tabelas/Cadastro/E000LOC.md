# E000LOC

## Descrição

Integrações - Varejo - Ligação O.P. com Cupom Fiscal

---

## Resumo

- Campos: 11
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeLoc | Number(009,0) | Não | Identificador de registro da ligação de O.P. com cupom fiscal |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Sim | Código da filial |
| CodSnf | String(003) | Sim | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |
| CodOri | String(003) | Não | Código da Origem |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Código da Derivação |
| QtdFat | Number(014,5) | Sim | Quantidade faturada do item da nota fiscal de saída |

---

## Chave Primária

- IdeLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
