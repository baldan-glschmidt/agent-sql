# R349FDA

## Descrição

S-5013 - eSocial - Informações de Depósitos de FGTS de períodos anteriores

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
| PerRef | Date | Não | Período Apuração |
| TipIns | String(001) | Não | Tipo do instrumento ou situação ensejadora da remuneração |
| SeqDat | Number(009,0) | Não | Sequência Período Anterior FGTS |
| TipDps | Number(002,0) | Sim | Tipo Depósito FGTS |
| ValDps | Number(014,2) | Sim | Valor do Depósito do FGTS |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- TipFol
- SeqTab
- PerRef
- TipIns
- SeqDat

---

## Índices

### R349FDAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
