# R350JCR

## Descrição

S-1210 - eSocial - Processos - não retenção de tributos/depósitos judiciais

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
| SeqJcr | Number(009,0) | Não | Sequência |
| TipPro | Number(001,0) | Sim | Código correspondente ao tipo de processo |
| NumPro | String(021) | Sim | Número do processo administrativo/judicial |
| CodSus | Number(014,0) | Sim | Código do indicativo da suspensão, atribuído pelo empregador em S-1070 |
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
- SeqJcr

---

## Índices

### R350JCRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
