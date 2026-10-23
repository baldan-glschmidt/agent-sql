# R349IBV

## Descrição

S-5013 - eSocial - Bases de cálculo e valores do FGTS em períodos anteriores

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
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| TipFol | Number(001,0) | Não | Tipo Folha |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIeo | Number(009,0) | Não | Sequência Identificação do Estabelecimento |
| SeqIlo | Number(009,0) | Não | Sequência Identificação da Lotação |
| SeqIbv | Number(009,0) | Não | Sequência da informação das bases e valores em períodos anteriores |
| PerRef | Date | Sim | Período ao qual se refere a remuneração |
| TipIns | String(001) | Sim | Tipo do instrumento ou situação ensejadora da remuneração |
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

---

## Índices

### R349IBVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
