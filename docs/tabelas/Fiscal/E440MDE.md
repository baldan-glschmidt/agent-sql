# E440MDE

## Descrição

Compras - Controle de eventos da manifestação do destinatário

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| TipEve | Number(006,0) | Não | Tipo do evento |
| SeqEve | Number(004,0) | Não | Sequência do evento |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| DesEve | String(060) | Sim | Descrição do evento |
| DatEve | Date | Não | Data do evento |
| HorEve | Number(005,0) | Não | Hora do evento |
| CodOrg | Number(002,0) | Sim | Código do órgão de recepção do evento |
| JusEve | String(254) | Sim | Justificativa do evento |
| SitEve | Number(002,0) | Sim | Situação do evento |
| UsuEve | Number(009,0) | Sim | Usuário solicitante do evento |
| PrtEve | String(015) | Sim | Número do protocolo de autorização do evento de manifestação do destinatário |
| CodMot | Number(006,0) | Sim | Código do motivo do evento de manifestação do destinatário |
| PrtAut | String(015) | Sim | Número do Protocolo de Autorização do Documento Fiscal Eletrônico |

---

## Chave Primária

- CodEmp
- CodFil
- ChvNel
- TipEve
- SeqEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440MDE_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

