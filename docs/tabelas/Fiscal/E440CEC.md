# E440CEC

## Descrição

Compras - Notas Fiscais de Entrada - Controle de eventos de documentos eletrônicos - Eventos do conhecimento de transporte eletrônico

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodFil | Number(005,0) | Não | Filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqEve | Number(004,0) | Não | Sequência do evento |
| TipEve | Number(006,0) | Não | Tipo do evento |
| SeqCec | Number(004,0) | Não | Sequência de evento do CT-e |
| GruAlt | String(040) | Não | Representa qual a descrição do grupo no XML que está sendo alterado |
| CamAlt | String(040) | Não | Representa qual a descrição do campo no XML que está sendo alterado |
| IteAlt | Number(002,0) | Sim | Representa qual o índice do grupo no XML que está sendo alterado |
| VlrAlt | String(499) | Não | Representa qual o novo valor que será considerado para o grupo e campo |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqEve
- TipEve
- SeqCec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440CEC_005

**Tabela:** E440CCE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |
| TipEve | TipEve |
| SeqEve | SeqEve |

