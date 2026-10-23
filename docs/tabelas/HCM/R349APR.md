# R349APR

## Descrição

S-5011 - eSocial - Informações relativas a aquisição de produção rural.

---

## Resumo

- Campos: 19
- Chave Primária: 7 campo(s)
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
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCeo | Number(009,0) | Não | Sequência |
| SeqApr | Number(009,0) | Não | Sequência |
| PrdAqu | Number(014,2) | Sim | Valor total da aquisição de produção rural de produtor rural |
| IndAqi | Number(001,0) | Sim | Indicativo da Aquisição |
| PrdCPD | Number(014,2) | Sim | Valor da Contribuição Previdenciária descontada pelo adquirente |
| PrdCPN | Number(014,2) | Sim | Valor da Contribuição Previdenciária que deixou de ser retida |
| PrdRaN | Number(014,2) | Sim | Valor da GILRAT, cuja retenção deixou de ser efetuada |
| PrdSeN | Number(014,2) | Sim | Valor da contribuição destinada ao SENAR que deixou de ser retida |
| PrdCPC | Number(014,2) | Sim | Valor calculado na contribuição previdenciária do produtor rural |
| PrdRaD | Number(014,2) | Sim | Valor da contribuição destinada ao financiamento de benefícios concedidos |
| PrdRaC | Number(014,2) | Sim | Valor calculado do RAT devido pelo Produtor Rural |
| PrdDSe | Number(014,2) | Sim | Valor da contribuição destinada ao SENAR |
| PrdCSe | Number(014,2) | Sim | Valor calculado da contribuição devida pelo produtor rural ao Senar |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo
- SeqApr

---

## Índices

### R349APRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
