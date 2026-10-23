# R349FIT

## Descrição

S-5003 - eSocial - Matrícula e Categoria do Trabalhador por Bases de FGTS

---

## Resumo

- Campos: 17
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqFel | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqFit | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| MatTra | String(030) | Sim | Matrícula do colaborador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| DatAdm | Date | Sim | Data de Admissão do Trabalhador |
| DatDes | Date | Sim | Data de Desligamento do Trabalhador |
| MotDes | Number(002,0) | Sim | Código do Motivo do Desligamento |
| DatIni | Date | Sim | Data de Início do TSV |
| DatTer | Date | Sim | Data de Término do TSV |
| MotDdi | Number(002,0) | Sim | Motivo do desligamento do Diretor Não Empregado |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqFel
- SeqFit

---

## Índices

### R349FITIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
