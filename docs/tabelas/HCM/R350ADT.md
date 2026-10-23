# R350ADT

## Descrição

S-2399 - eSocial - Identificação dos advogados

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
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
| SeqRsv | Number(009,0) | Não | Sequência |
| SeqPsv | Number(009,0) | Não | Sequência |
| SeqAdt | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do Advogado |
| NumIns | Number(014,0) | Sim | Número de inscrição do Advogado |
| CfjIns | String(014) | Sim | Número de inscrição do Advogado |
| ValAdv | Number(014,2) | Sim | Valor da despesa com advogados |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqRsv
- SeqPsv
- SeqAdt

---

## Índices

### R350ADTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
