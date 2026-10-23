# R350NFC

## Descrição

S-1260 - eSocial - Registro Detalha Notas Fiscais de Comercialização de Produção

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
| SeqCom | Number(009,0) | Não | Sequência |
| SeqVtc | Number(009,0) | Não | Sequência |
| SeqIap | Number(009,0) | Não | Sequência |
| SeqNfc | Number(009,0) | Não | Sequência |
| NumSer | String(005) | Sim | Número de série da nota fiscal/fatura |
| NumNot | String(020) | Sim | Número da Nota Fiscal/Fatura |
| DatEmi | Date | Sim | Data de Emissão da Nota Fiscal/Fatura |
| ValBru | Number(014,2) | Sim | Valor bruto da(s) nota(s) fiscal(is) |
| ValPre | Number(014,2) | Sim | Valor da contribuição destinada ao financiamento dos benefícios |
| ValFin | Number(014,2) | Sim | Valor da contribuição destinada ao financiamento dos benefícios |
| ValSen | Number(014,2) | Sim | Valor da contribuição destinada ao SENAR |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqCom
- SeqVtc
- SeqIap
- SeqNfc

---

## Índices

### R350NFCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
