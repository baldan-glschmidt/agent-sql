# R350IPR

## Descrição

S-1250 - eSocial - Registro Identifica Produtoras Rurais Aquisição Rural

---

## Resumo

- Campos: 16
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
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqAqu | Number(009,0) | Não | Sequência |
| SeqEap | Number(009,0) | Não | Sequência |
| SeqIpr | Number(009,0) | Não | Sequência |
| TipAqu | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumAqu | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjAqu | String(014) | Sim | Número de inscrição do contribuinte |
| ValBru | Number(014,2) | Sim | Valor bruto da(s) nota(s) fiscal(is) |
| ValCon | Number(014,2) | Sim | Valor da Contribuição Previdenciária |
| ValFin | Number(014,2) | Sim | Valor da contribuição destinada ao financiamento dos benefícios |
| VSENAR | Number(014,2) | Sim | Valor da contribuição destinada ao SENAR |
| OpcPRu | Number(002,0) | Sim | Opção pelo produtor rural de tributação da contribuição previdenciária |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqAqu
- SeqEap
- SeqIpr

---

## Índices

### R350IPRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
