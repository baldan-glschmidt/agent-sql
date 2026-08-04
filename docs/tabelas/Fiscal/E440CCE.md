# E440CCE

## Descrição

Compras - Notas Fiscais de Entrada - Controle de eventos de documentos eletrônicos

---

## Resumo

- Campos: 22
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqEve | Number(004,0) | Não | Sequência do evento |
| TipEve | Number(006,0) | Não | Tipo do evento |
| DesEve | String(100) | Sim | Descrição do evento |
| DatEve | Date | Sim | Data do evento |
| HorEve | Number(005,0) | Sim | Hora do evento |
| UsuEve | Number(009,0) | Sim | Usuário solicitante do evento |
| CodOrg | Number(002,0) | Sim | Código do órgão de recepção do evento |
| DesCor | String(999) | Sim | Descritivo da correção a ser considerada |
| SitCce | Number(002,0) | Não | Situação do evento |
| NumPrt | String(017) | Sim | Número do protocolo |
| DatAut | Date | Sim | Data da protocolo |
| HorAut | Number(005,0) | Sim | Hora da protocolo |
| JusEve | String(254) | Sim | Justificativa do evento |
| RelSeq | Number(004,0) | Sim | Sequência do Evento Relacionado |
| RelTip | Number(006,0) | Sim | Tipo do Evento Relacionado |
| RelPrt | String(017) | Sim | Número do protocolo do Evento Relacionado |
| IndApr | String(001) | Sim | Indicador de concordância |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- TipEve
- SeqEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440CCE_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E440CCE_002

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E440CCE_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

