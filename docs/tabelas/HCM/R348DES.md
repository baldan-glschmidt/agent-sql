# R348DES

## Descrição

eSocial - GRFGTS - Visão Remuneração - Trabalhadores Desligados - obsoleta

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| SeqDES | Number(009,0) | Não | Sequência |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| NomTra | String(200) | Sim | Nome do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| MatTra | String(050) | Sim | Matrícula |
| DatDes | Date | Sim | Data de desligamento |
| CodMot | Number(002,0) | Sim | Código do motivo de desligamento |
| DesMot | String(200) | Sim | Descrição do motivo de desligamento |
| DatAdm | Date | Sim | Data de admissão |
| CodCat | Number(004,0) | Sim | Categoria eSocial |
| DesCat | String(200) | Sim | Descrição da categoria eSocial |

---

## Chave Primária

- IdePen
- SeqDES

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
