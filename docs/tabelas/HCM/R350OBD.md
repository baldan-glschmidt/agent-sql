# R350OBD

## Descrição

S-2299 - eSocial - Observações sobre o desligamento

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqDes | Number(009,0) | Não | Sequência |
| SeqObd | Number(009,0) | Não | Sequência |
| ObsDes | String(255) | Sim | Observações sobre o desligamento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqObd

---

## Índices

### R350OBDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
