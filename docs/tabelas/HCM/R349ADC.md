# R349ADC

## Descrição

S-5001 - eSocial - Instrumento ou situação ensejadora da remuneração em períodos anteriores

---

## Resumo

- Campos: 15
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
| SeqElt | Number(009,0) | Não | Sequência |
| SeqMct | Number(009,0) | Não | Sequência |
| SeqIrp | Number(009,0) | Não | Sequência |
| SeqAdc | Number(009,0) | Não | Sequência |
| DatAco | Date | Sim | Data da assinatura do acordo, convenção coletiva, sentença normativa ou da conversão da licença saúde em acidente de trabalho |
| TipAco | String(001) | Sim | Tipo do instrumento ou situação ensejadora da remuneração relativa a períodos de apuração anteriores |
| DscIns | String(255) | Sim | Descrição do instrumento ou situação que originou o pagamento das verbas relativas a períodos anteriores |
| RemSuc | String(001) | Sim | Indicar se a remuneração é relativa a verbas devidas pela empresa sucessora |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- CpfTra
- SeqTab
- SeqElt
- SeqMct
- SeqIrp
- SeqAdc

---

## Índices

### R349ADCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
