# R349BCR

## Descrição

S-5011 - eSocial - Bases de cálculo por categoria

---

## Resumo

- Campos: 41
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
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCeo | Number(009,0) | Não | Sequência |
| SeqCle | Number(009,0) | Não | Sequência |
| SeqBcr | Number(009,0) | Não | Sequência |
| TipInc | Number(001,0) | Sim | Cód correspondente ao tipo de incidência para apuração da contrib previdenciária |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| BcCp00 | Number(014,2) | Sim | Base de cálculo da contribuição previdenciária |
| BcCp15 | Number(014,2) | Sim | Base de cálculo da Contrib Prev - adicional aposentadoria especial 15 anos |
| BcCp20 | Number(014,2) | Sim | Base de cálculo da Contrib Prev - adicional aposentadoria especial 20 anos |
| BcCp25 | Number(014,2) | Sim | Base de cálculo da Contrib Prev - adicional aposentadoria especial 25 anos |
| SuCp00 | Number(014,2) | Sim | Valor da BC com incidência suspensa |
| SuCp15 | Number(014,2) | Sim | Valor da BC com incidência suspensa aposentadoria especial 15 anos |
| SuCp20 | Number(014,2) | Sim | Valor da BC com incidência suspensa aposentadoria especial 20 anos |
| SuCp25 | Number(014,2) | Sim | Valor da BC com incidência suspensa aposentadoria especial 25 anos |
| BcVa00 | Number(014,2) | Sim | Base de cálculo da contribuição previdenciária - Contrato Verde/Amarelo |
| BcVa15 | Number(014,2) | Sim | Base de cálculo da Contrib Prev - adicional aposentadoria especial 15 anos - Contrato Verde/Amarelo |
| BcVa20 | Number(014,2) | Sim | Base de cálculo da Contrib Prev - adicional aposentadoria especial 20 anos - Contrato Verde/Amarelo |
| BcVa25 | Number(014,2) | Sim | Base de cálculo da Contrib Prev - adicional aposentadoria especial 25 anos - Contrato Verde/Amarelo |
| SuVa00 | Number(014,2) | Sim | Valor da BC com incidência suspensa - Contrato Verde/Amarelo |
| SuVa15 | Number(014,2) | Sim | Valor da BC com incidência suspensa aposentadoria especial 15 anos - Contrato Verde/Amarelo |
| SuVa20 | Number(014,2) | Sim | Valor da BC com incidência suspensa aposentadoria especial 20 anos - Contrato Verde/Amarelo |
| SuVa25 | Number(014,2) | Sim | Valor da BC com incidência suspensa aposentadoria especial 25 anos - Contrato Verde/Amarelo |
| DesSes | Number(014,2) | Sim | Valor total descontado do trabalhador para recolhimento ao Sest |
| CalSes | Number(014,2) | Sim | Valor da contribuição devida pelo trabalhador para recolhimento ao Sest |
| DesSen | Number(014,2) | Sim | Valor total descontado do trabalhador para recolhimento ao Senat |
| CalSen | Number(014,2) | Sim | Valor da contribuição devida pelo trabalhador para recolhimento ao Senat |
| SalFam | Number(014,2) | Sim | Valor total do salário-família para a categoria |
| SalMat | Number(014,2) | Sim | Valor total do salário-maternidade para a categoria |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| B13C00 | Number(014,2) | Sim | Base de cálculo da contribuição previdenciária - 13º Salário |
| B13C15 | Number(014,2) | Sim | Base de cálculo da contrib prev adicional apos. especial 15 anos - 13º Salário |
| B13C20 | Number(014,2) | Sim | Base de cálculo da contrib prev adicional apos. especial 20 anos - 13º Salário |
| B13C25 | Number(014,2) | Sim | Base de cálculo da contrib prev adicional apos. especial 25 anos - 13º Salário |
| S13C00 | Number(014,2) | Sim | Base cálculo incidência suspensa - 13º Salário |
| S13C15 | Number(014,2) | Sim | Base cálculo incidência suspensa aposentadoria especial 15 anos - 13º Salário |
| S13C20 | Number(014,2) | Sim | Base cálculo incidência suspensa aposentadoria especial 20 anos - 13º Salário |
| S13C25 | Number(014,2) | Sim | Base cálculo incidência suspensa aposentadoria especial 25 anos - 13º Salário |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo
- SeqCle
- SeqBcr

---

## Índices

### R349BCRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
