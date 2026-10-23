# R350VTC

## Descrição

S-1260 - eSocial - Valor total da comercialização por "tipo" de comercialização

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
| SeqCom | Number(009,0) | Não | Sequência |
| SeqVtc | Number(009,0) | Não | Sequência |
| IndCom | Number(001,0) | Sim | Indicativo de Comercialização |
| ValCom | Number(014,2) | Sim | Valor total da comercialização |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqCom
- SeqVtc

---

## Índices

### R350VTCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
