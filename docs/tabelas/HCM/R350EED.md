# R350EED

## Descrição

S-1005 - eSocial - Entidade Educativa/Prática Desportiva

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| SeqEst | Number(009,0) | Não | Sequência |
| SeqEEd | Number(009,0) | Não | Sequência |
| NumIns | Number(014,0) | Sim | Número de inscrição da Entidade Educativa/Prática Desportiva |
| CfjIns | String(014) | Sim | Número de inscrição da Entidade Educativa/Prática Desportiva |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |

---

## Chave Primária

- NumEmp
- FilEmp
- SeqEst
- SeqEEd

---

## Índices

### R350EEDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
