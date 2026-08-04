# E440SEG

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Manifesto Seguro da Carga

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqSeg | Number(004,0) | Não | Sequência do seguro da carga |
| RepSeg | Number(001,0) | Sim | Responsável pelo seguro (MDF-e) |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ/CPF do responsável pelo seguro |
| DocIdeRep | String(014) | Sim | Número do CNPJ/CPF do responsável pelo seguro |
| CodSeg | Number(009,0) | Sim | Código da Seguradora |
| NumApo | String(060) | Sim | Numero da apólice do seguro |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfc
- SeqSeg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
