# R108REA

## Descrição

Resultados Exames Audiometria - Complemento Resultados

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| CodFic | Number(009,0) | Não | Ficha Médica |
| CodExa | Number(004,0) | Não | Código do Exame |
| DatSol | Date | Não | Data da Solicitação |
| SeqIex | Number(003,0) | Não |  |
| IndMas | String(001) | Sim | Indicador de Mascaramento |
| CodMas | Number(003,0) | Sim | Tipo do Mascaramento |
| IndRes | String(001) | Sim | Indica se houve resposta |
| IndTes | String(001) | Sim | Indica se houve teste nesta frequência. |

---

## Chave Primária

- NumEmp
- CodFic
- CodExa
- DatSol
- SeqIex

---

## Índices

### R108REAindice2

**Tipo:** Não unico

Campos:
- CodExa

---

## Relacionamentos

Nenhum relacionamento cadastrado.
