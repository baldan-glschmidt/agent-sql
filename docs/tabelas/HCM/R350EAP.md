# R350EAP

## Descrição

S-1250 - eSocial - Registro por Tipo de Aquisição Rural

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
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
| IndAqu | Number(001,0) | Sim | Indicativo da Aquisição |
| ValAqu | Number(014,2) | Sim | Valor total da aquisição correspondente ao indicativo informado |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqAqu
- SeqEap

---

## Índices

### R350EAPindice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
