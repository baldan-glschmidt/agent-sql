# R350PCO

## Descrição

S-1260 - eSocial - Registro Processo de Comercialização de Produção

---

## Resumo

- Campos: 14
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
| SeqCom | Number(009,0) | Não | Sequência |
| SeqVtc | Number(009,0) | Não | Sequência |
| SeqPro | Number(009,0) | Não | Sequência |
| TipPro | Number(001,0) | Sim | Código Correspondente ao Tipo do Processo |
| NumPro | String(021) | Sim | Número do Processo |
| CodSus | Number(014,0) | Sim | Código Suspensão |
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
- SeqCom
- SeqVtc
- SeqPro

---

## Índices

### R350PCOIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
