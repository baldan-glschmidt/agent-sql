# E440VPE

## Descrição

Compras - Nota Fiscal de Entrada - Manifesto de Documentos Fiscais - Vale Pedágio

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| SeqVpe | Number(004,0) | Não | Sequência do vale pedágio |
| CodFor | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada |
| CgcFor | Number(014,0) | Sim | Número do CNPJ da empresa fornecedora do vale pedágio |
| DocIdeFor | String(014) | Sim | Número do CNPJ da empresa fornecedora do vale pedágio |
| NumCom | String(020) | Sim | Número do comprovante de compra do vale pedágio |
| CodCli | Number(009,0) | Sim | Código do cliente da nota fiscal de entrada |
| CgcPag | Number(014,0) | Sim | Número do CNPJ da empresa pagadora do vale pedágio |
| DocIdePag | String(014) | Sim | Número do CNPJ da empresa pagadora do vale pedágio |
| VlrVpe | Number(015,2) | Sim | Valor do vale pedágio |
| TipVpe | Number(002,0) | Sim | Tipo do Vale Pedágio |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfc
- SeqVpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440VPE_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

