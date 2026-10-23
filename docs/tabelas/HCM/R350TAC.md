# R350TAC

## Descrição

S-2206 - eSocial - Alteração de Contrato de Trabalho/Relação Estatutária - Treinamentos

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
| SeqAco | Number(009,0) | Não | Sequência |
| SeqTac | Number(009,0) | Não | Sequência |
| CodTce | Number(004,0) | Sim | Código do treinamento na tabela 28 do eSocial |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAco
- SeqTac

---

## Índices

### R350TACIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
