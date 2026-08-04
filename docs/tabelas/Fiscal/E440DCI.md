# E440DCI

## Descrição

Compras - Notas Fiscais de Entrada - Detalhamento por Classificação dos Itens

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| SeqCla | Number(003,0) | Não | Sequencia do Detalhamento |
| CodCla | String(020) | Não | Código de classificação do item |
| VlrCla | Number(015,2) | Não | Valor do Detalhamento |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqCla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440DCI_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

