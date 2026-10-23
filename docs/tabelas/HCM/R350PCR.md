# R350PCR

## Descrição

S-1210 - eSocial - Informação dos beneficiários da pensão alimentícia

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqRcr | Number(009,0) | Não | Sequência |
| SeqPcr | Number(009,0) | Não | Sequência |
| TipRen | Number(002,0) | Sim | Tipo de Rendimento |
| CpfDep | Number(011,0) | Sim | CPF do Dependente |
| VlrPen | Number(014,2) | Sim | Valor relativo à dedução do rendimento tributável correspondente a pagamento de pensão alimentícia |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqRcr
- SeqPcr

---

## Índices

### R350PCRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
