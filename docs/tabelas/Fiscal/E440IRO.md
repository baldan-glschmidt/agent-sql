# E440IRO

## Descrição

Compras - Notas Fiscais de Entrada - Créditos de Royalties dos Itens de Produto

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| QtdRoy | Number(014,5) | Sim | Quantidade total de royalties do item da nota |
| CreUti | Number(014,5) | Sim | Quantidade de crédito de Royalties do item da nota |
| VlrRoy | Number(014,5) | Sim | Valor do desconto de Royalties do item da Nota |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440IRO_005

**Tabela:** E440IPC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| SeqIpc | SeqIpc |

