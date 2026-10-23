# R350NFA

## Descrição

S-1250 - eSocial - Registro Detalha as Notas Fiscais de Aquisição da Produção

---

## Resumo

- Campos: 16
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
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqAqu | Number(009,0) | Não | Sequência |
| SeqEap | Number(009,0) | Não | Sequência |
| SeqIpr | Number(009,0) | Não | Sequência |
| SeqNfa | Number(009,0) | Não | Sequência |
| NumSer | String(005) | Sim | Número de série da nota fiscal/fatura |
| NumNFi | String(020) | Sim | Número da Nota Fiscal/Fatura |
| DatEmi | Date | Sim | Data de Emissão da Nota Fiscal/Fatura |
| ValBru | Number(014,2) | Sim | Valor bruto da(s) nota(s) fiscal(is) |
| ValCon | Number(014,2) | Sim | Valor da contribuição destinada ao financiamento dos benefícios |
| ValFin | Number(014,2) | Sim | Valor da contribuição destinada ao financiamento dos benefícios |
| VSENAR | Number(014,2) | Sim | Valor da contribuição destinada ao SENAR |
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
- SeqNfa

---

## Índices

### R350NFAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
