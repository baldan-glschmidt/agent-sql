# R350RTP

## Descrição

S-1210 - eSocial - Reembolso do titular do plano de saúde coletivo empresarial

---

## Resumo

- Campos: 14
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
| SeqRps | Number(009,0) | Não | Sequência |
| SeqRtp | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do prestador de serviços |
| NumIns | Number(014,0) | Sim | Número de inscrição do prestador de serviços de assistência médica |
| CfjIns | String(014) | Sim | Número de inscrição do prestador de serviços de assistência médica |
| VlReAt | Number(014,2) | Sim | Valor do reembolso relativo ao período indicado em perApur |
| VlReAn | Number(014,2) | Sim | Valor do reembolso relativo a anos anteriores |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqRps
- SeqRtp

---

## Índices

### R350RTPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
