# R349FAD

## Descrição

S-5003 - eSocial - Depósitos de FGTS em Períodos Anteriores

---

## Resumo

- Campos: 13
- Chave Primária: 10 campo(s)
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
| SeqFdt | Number(009,0) | Não | Sequência Matrícula e Categoria do Trabalhador |
| PerRef | Date | Não | Período Apuração |
| TipIns | String(001) | Não | Tipo do instrumento ou situação ensejadora da remuneração |
| SeqFad | Number(009,0) | Não | Sequência dos Depósitos em Períodos Anteriores |
| TipDps | Number(002,0) | Sim | Tipo Depósito FGTS |
| ValDps | Number(014,2) | Sim | Valor do Depósito de FGTS |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqFdt
- PerRef
- TipIns
- SeqFad

---

## Índices

### R349FADIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
