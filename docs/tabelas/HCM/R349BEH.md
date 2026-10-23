# R349BEH

## Descrição

S-5013 - eSocial - Bases de cálculo e valores do FGTS períodos anteriores

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
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
| SeqIeo | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqIlo | Number(009,0) | Não | Sequência Identificação da Lotação |
| SeqIbv | Number(009,0) | Não | Sequência da informação das bases e valores em períodos anteriores |
| SeqBeh | Number(009,0) | Não | Sequência da informação das bases e valores em períodos anteriores |
| TipVal | Number(002,0) | Sim | Tipo de valor que influi na apuração do FGTS |
| IndInc | Number(001,0) | Sim | Indicativo de incidência de FGTS |
| ValBas | Number(014,2) | Sim | Valor da base de cálculo do FGTS |
| ValHis | Number(014,2) | Sim | Valor histórico do FGTS a ser depositado |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- TipFol
- SeqTab
- SeqIeo
- SeqIlo
- SeqIbv
- SeqBeh

---

## Índices

### R349BEHIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
