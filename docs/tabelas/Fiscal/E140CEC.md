# E140CEC

## Descrição

Vendas - Notas Fiscais de Saída - Controle de eventos de documentos eletrônicos - Eventos do conhecimento de transporte eletrônico

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodFil | Number(005,0) | Não | Filial |
| CodSnf | String(003) | Não | Série |
| NumNfv | Number(009,0) | Não | Número da nota fiscal |
| SeqEve | Number(004,0) | Não | Sequência do evento de documento eletrônico |
| TipEve | Number(006,0) | Não | Tipo de evento |
| SeqCec | Number(004,0) | Não | Sequência de evento do CT-e |
| GruAlt | String(040) | Não | Representa qual a descrição do grupo no XML que está sendo alterado |
| CamAlt | String(040) | Não | Representa qual a descrição do campo no XML que está sendo alterado |
| IteAlt | Number(002,0) | Sim | Representa qual o índice do grupo no XML que está sendo alterado |
| VlrAlt | String(499) | Não | Representa qual o novo valor que será considerado para o grupo e campo |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqEve
- TipEve
- SeqCec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CEC_004

**Tabela:** E140CCE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| TipEve | TipEve |
| SeqEve | SeqEve |

