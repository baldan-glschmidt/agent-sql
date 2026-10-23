# R350PSD

## Descrição

S-1210 - eSocial - Dependente de plano de saúde coletivo empresarial

---

## Resumo

- Campos: 11
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
| SeqPsc | Number(009,0) | Não | Sequência |
| SeqPsd | Number(009,0) | Não | Sequência |
| CpfDep | Number(011,0) | Sim | Número de inscrição no CPF do dependente do plano de saúde |
| VlrDep | Number(014,2) | Sim | Valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do dependente |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqPsc
- SeqPsd

---

## Índices

### R350PSDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
