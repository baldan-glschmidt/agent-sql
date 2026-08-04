# E440UNC

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Manifesto Unidades de Carga

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
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
| SeqImd | Number(003,0) | Não | Sequência do item no manifesto |
| SeqUnt | Number(004,0) | Não | Sequência da unidade de transporte |
| SeqUnc | Number(004,0) | Não | Sequência da unidade de carga |
| TipUnc | Number(001,0) | Não | Tipo da unidade de carga |
| CodIdc | String(040) | Não | Código de identificação da unidade de carga |
| VlrRat | Number(006,3) | Sim | Valor da quantidade rateada (Peso, Volume) |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfc
- SeqImd
- SeqUnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
