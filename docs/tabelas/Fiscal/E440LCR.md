# E440LCR

## Descrição

Compra/Serviços - Notas Fiscais de Entrada - Itens de Produto - Ligação Entre Itens de Produto de Notas Fiscais de Entrada por Compra/Serviço e Retorno.

---

## Resumo

- Campos: 16
- Chave Primária: 13 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial da nota fiscal de entrada por Compra/Serviço |
| CodFor | Number(009,0) | Não | Fornecedor da nota fiscal de entrada por Compra/Serviço |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada por Compra/Serviço |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada por Compra/Serviço |
| SeqIpc | Number(003,0) | Não | Sequência do item da nota fiscal de entrada por Compra/Serviço |
| SeqIsc | Number(003,0) | Não | Sequência do item da nota fiscal de entrada por Compra/Serviço |
| EmpNrc | Number(004,0) | Não | Código da empresa da nota fiscal de entrada por retorno |
| FilNrc | Number(005,0) | Não | Código da filial da nota fiscal de entrada por retorno |
| ForNrc | Number(009,0) | Não | Fornecedor da nota fiscal de entrada por retorno |
| NumNrc | Number(009,0) | Não | Número da nota fiscal de entrada por retorno |
| SnfNrc | String(003) | Não | Código da série da nota fiscal de entrada por retorno |
| IpcNrc | Number(003,0) | Não | Sequência do item da nota fiscal de entrada por retorno |
| QtdRci | Number(014,5) | Sim | Quantidade retornada da Compra/Serviço na nota fiscal de retorno |
| QtdDev | Number(014,5) | Sim | Quantidade devolvida da NF de entrada por retorno de industrialização |
| TipLcr | String(001) | Sim | Tipo de ligação de Itens de Nota Fiscal |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc
- SeqIsc
- EmpNrc
- FilNrc
- ForNrc
- NumNrc
- SnfNrc
- IpcNrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
