# R349FBC

## Descrição

S-5013 - eSocial - Informações consolidadas das bases de cálculo do FGTS

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
| TipFol | Number(001,0) | Não | Tipo Folha |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqBap | Number(009,0) | Não | Sequência bases de cálculo do FGTS do período apuração |
| TipBas | Number(002,0) | Sim | Tipo Base FGTS |
| ValBas | Number(014,2) | Sim | Valor da base de cálculo do FGTS |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- TipFol
- SeqTab
- SeqBap

---

## Índices

### R349FBCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
