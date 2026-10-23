# R349DRE

## Descrição

S-5002 - eSocial - Informação de reembolso do titular do plano de saúde

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
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqRee | Number(009,0) | Não | Sequência |
| SeqDre | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição do Prestador de Serviços de Assistência Médica |
| NumIns | Number(014,0) | Sim | Número de Inscrição do Prestador de Serviços de Assistência Médica |
| CfjIns | String(014) | Sim | Número de Inscrição do Prestador de Serviços de Assistência Médica |
| VlrRee | Number(014,2) | Sim | Valor do Reembolso Relativo ao Período Indicado |
| VlrRea | Number(014,2) | Sim | Valor do Reembolso Relativo a Anos Anteriores |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqRee
- SeqDre

---

## Índices

### R349DREIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
