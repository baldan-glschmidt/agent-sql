# E140SEG

## Descrição

Vendas - Notas Fiscais de Saída - Informações de seguro

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqSeg | Number(004,0) | Não | Sequência do seguro da carga |
| CodSeg | Number(009,0) | Sim | Código da Seguradora |
| ResSeg | Number(001,0) | Sim | Responsável pelo seguro (CT-e) |
| NumAvb | String(060) | Sim | Número da averbação. (CT-e) |
| VlrAvb | Number(015,6) | Sim | Valor para efeito de averbação |
| NumApo | String(060) | Sim | Numero da apólice do seguro |
| RepSeg | Number(001,0) | Sim | Responsável pelo seguro (MDF-e) |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ/CPF do responsável pelo seguro (MDF-e) |
| DocIde | String(014) | Sim | Número do CNPJ/CPF do responsável pelo seguro (MDF-e) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
