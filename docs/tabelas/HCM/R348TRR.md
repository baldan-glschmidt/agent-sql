# R348TRR

## Descrição

eSocial - GRFGTS - Visão Remuneração - Trab. Recolhido Rescisório - obsoleta

---

## Resumo

- Campos: 26
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| SeqTRR | Number(009,0) | Não | Sequência |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| NomTra | String(200) | Sim | Nome do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| CodCat | Number(004,0) | Sim | Categoria eSocial |
| MatTra | String(050) | Sim | Matrícula |
| DatAdm | Date | Sim | Data de admissão |
| IdeGui | String(050) | Sim | Identificador da guia |
| DatPag | Date | Sim | Data de pagamento |
| RcsMes | Number(014,2) | Sim | Mês rescisão |
| Rcs13s | Number(014,2) | Sim | Mês rescisão 13º |
| ValDis | Number(014,2) | Sim | Dissídio |
| Val13d | Number(014,2) | Sim | Dissídio 13º |
| MulRes | Number(014,2) | Sim | Multa rescisória |
| ConSoc | Number(014,2) | Sim | Contribuição social |
| ValInd | Number(014,2) | Sim | Verbas indenizatórias |
| TotPag | Number(014,2) | Sim | Total recolhido |
| FgtJur | Number(014,2) | Sim | FGTS - Juros |
| FgtMon | Number(014,2) | Sim | FGTS - Atualização monetária |
| FgtMul | Number(014,2) | Sim | FGTS - Multa |
| SocJur | Number(014,2) | Sim | Contribuição social - Juros |
| SocMon | Number(014,2) | Sim | Contribuição social - Atualização monetária |
| SocMul | Number(014,2) | Sim | Contribuição social - Multa |

---

## Chave Primária

- IdePen
- SeqTRR

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
