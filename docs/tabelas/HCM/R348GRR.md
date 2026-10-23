# R348GRR

## Descrição

eSocial - GRFGTS - Visão Remuneração - Trab. Recolher Rescisório - obsoleta

---

## Resumo

- Campos: 29
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| SeqGRR | Number(009,0) | Não | Sequência |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| IdeGui | String(050) | Sim | Identificador da guia |
| SitGui | String(050) | Sim | Situação da guia |
| NomTra | String(200) | Sim | Nome do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| CodCat | Number(004,0) | Sim | Categoria eSocial |
| MatTra | String(050) | Sim | Matrícula |
| DatAdm | Date | Sim | Data de admissão |
| DatDes | Date | Sim | Data de desligamento |
| CodMot | Number(002,0) | Sim | Código do motivo de desligamento |
| DesMot | String(200) | Sim | Descrição do motivo de desligamento |
| RcsMes | Number(014,2) | Sim | Mês rescisão |
| Rcs13s | Number(014,2) | Sim | Mês rescisão 13º |
| ValDis | Number(014,2) | Sim | Dissídio |
| Val13d | Number(014,2) | Sim | Dissídio 13º |
| MulRes | Number(014,2) | Sim | Multa rescisória |
| ConSoc | Number(014,2) | Sim | Contribuição social |
| ValInd | Number(014,2) | Sim | Verbas indenizatórias |
| TotDev | Number(014,2) | Sim | Total recolher |
| FgtJur | Number(014,2) | Sim | FGTS - Juros |
| FgtMon | Number(014,2) | Sim | FGTS - Atualização monetária |
| FgtMul | Number(014,2) | Sim | FGTS - Multa |
| SocJur | Number(014,2) | Sim | Contribuição social - Juros |
| SocMon | Number(014,2) | Sim | Contribuição social - Atualização monetária |
| SocMul | Number(014,2) | Sim | Contribuição social - Multa |

---

## Chave Primária

- IdePen
- SeqGRR

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
