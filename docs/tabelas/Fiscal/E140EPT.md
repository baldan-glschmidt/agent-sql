# E140EPT

## Descrição

Vendas - Notas Fiscais Saída - Embalagens/Produtos para Transferência

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpOri | Number(004,0) | Não | Código da empresa origem |
| FilOri | Number(005,0) | Não | Código da filial de origem |
| EmpDes | Number(004,0) | Não | Código da empresa destino |
| FilDes | Number(005,0) | Não | Código da filial de destino |
| PlaVei | String(010) | Não | Placa do veículo utilizado para o transporte dos produtos da nota de transferência (Identificador para o processo) |
| SeqEpt | Number(009,0) | Não | Seqüência de controle |
| NumEmb | String(030) | Sim | Número da embalagem de estocagem |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do produto |
| QtdPro | Number(014,5) | Sim | Quantidade do produto |
| SitEpt | Number(001,0) | Não | Situação do registro |

---

## Chave Primária

- EmpOri
- FilOri
- EmpDes
- FilDes
- PlaVei
- SeqEpt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
