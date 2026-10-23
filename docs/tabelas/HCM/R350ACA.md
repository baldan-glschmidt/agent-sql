# R350ACA

## Descrição

S-2210 - eSocial - Detalhamento do(s) agente(s) causador(es) do acidente de trabalho (Obsoleta)

---

## Resumo

- Campos: 11
- Chave Primária: 9 campo(s)
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
| DatAct | Date | Não | Data Acidente de Trabalho |
| HorAct | Number(005,0) | Não | Hora Acidente de Trabalho |
| DatCat | Date | Não | Data de registro da  CAT |
| SeqCat | Number(009,0) | Não | Sequência |
| SeqAca | Number(009,0) | Não | Sequência |
| CodACa | Number(009,0) | Sim | Código correspondente ao agente causador |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatAct
- HorAct
- DatCat
- SeqCat
- SeqAca

---

## Índices

### R350ACAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
