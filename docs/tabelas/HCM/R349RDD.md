# R349RDD

## Descrição

S-5002 - eSocial - Detalhamento dos reembolsos efetuados aos dependentes

---

## Resumo

- Campos: 15
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 1

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
| SeqRed | Number(009,0) | Não | Sequência |
| SeqRdd | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
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
- SeqRed
- SeqRdd

---

## Índices

### R349RDDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

### IR_R349RDD_007

**Tabela:** R349RED

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| FilEmp | FilEmp |
| PerApu | PerApu |
| CpfTra | CpfTra |
| SeqTab | SeqTab |
| SeqCpl | SeqCpl |
| SeqRee | SeqRee |
| SeqRed | SeqRed |

