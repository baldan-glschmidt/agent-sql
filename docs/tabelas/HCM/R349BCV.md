# R349BCV

## Descrição

S-5013 - eSocial - Bases de cálculo e valores do FGTS

---

## Resumo

- Campos: 13
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
| TipFol | Number(001,0) | Não | Tipo Folha |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIeo | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqIlo | Number(009,0) | Não | Sequência Identificação da Lotação |
| SeqBcv | Number(009,0) | Não | Sequência bases de cálculo do FGTS do período apuração |
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
- SeqBcv

---

## Índices

### R349BCVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
