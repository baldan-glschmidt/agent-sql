# R350INF

## Descrição

S-1210 - eSocial - Informações Complementares

---

## Resumo

- Campos: 10
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
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| DatLau | Date | Sim | Data da moléstia grave atribuída pelo laudo |
| PerAnt | Date | Sim | Período anterior |
| NumRec | String(040) | Sim | Número do recibo do S-1210 original cujas informações complem. serão alteradas |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf

---

## Índices

### R350INFIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
