# R350RPS

## Descrição

S-1210 - eSocial - Reembolsos desp. médicas/odontológicas no período de apuração

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
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
| IndOri | Number(001,0) | Sim | Indicativo da origem do reembolso |
| CnpjOp | Number(014,0) | Sim | CNPJ da operadora do plano de saúde |
| CfjIns | String(014) | Sim | CNPJ da operadora de plano privado coletivo empresarial de assistência à saúde |
| RegANS | Number(006,0) | Sim | Registro na Agência Nacional de Saúde |
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

---

## Índices

### R350RPSIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
