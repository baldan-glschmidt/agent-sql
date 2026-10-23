# R349BDI

## Descrição

S-5002 - eSocial - Rendimentos tributáveis, deduções, isenções e retenções do IR

---

## Resumo

- Campos: 11
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIdv | Number(009,0) | Não | Sequência |
| SeqBdi | Number(009,0) | Não | Sequência |
| TipInf | Number(004,0) | Sim | Consolidação dos tipos de valores relativos ao IRRF |
| ValRen | Number(014,2) | Sim | Composição do valor do rendimento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| DesRen | String(100) | Sim | Descrição do rendimento não tributável ou isento do IRRF |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIdv
- SeqBdi

---

## Índices

### R349BDIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
