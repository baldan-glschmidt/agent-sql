# R350PEM

## Descrição

S-1200 - eSocial - Pendências Envio Declaração Mensal

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidPem | String(035) | Não | Identificador da execução da pendência |
| NumEmp | Number(004,0) | Sim | Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| CmpRef | Date | Sim | Período Apuração |
| TipFol | Number(001,0) | Sim | Tipo Folha |
| OriPem | Number(001,0) | Sim | Origem da Pendência |
| CodFil | Number(006,0) | Não | Código da Filial |
| LayOut | String(006) | Sim | Leiaute |

---

## Chave Primária

- PidPem

---

## Índices

### R350PEMIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CmpRef
- TipFol

---

## Relacionamentos

Nenhum relacionamento cadastrado.
