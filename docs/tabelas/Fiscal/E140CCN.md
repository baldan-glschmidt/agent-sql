# E140CCN

## Descrição

Vendas - Notas Fiscais de Saída - Notas fiscais referenciadas a eventos de documentos eletrônicos

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqEve | Number(004,0) | Não | Sequência do evento |
| TipEve | Number(006,0) | Não | Tipo do evento |
| NumNfr | Number(009,0) | Não | Número da nota fiscal de saída |
| ChvNrf | String(050) | Sim | Chave de acesso da NF-e com insucesso na tentativa de entrega |
| UsuEve | Number(010,0) | Sim | Usuário solicitante do evento |
| SeqEnt | Number(004,0) | Sim | Sequência do registro de entrega |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- TipEve
- SeqEve
- NumNfr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CCN_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E140CCN_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

