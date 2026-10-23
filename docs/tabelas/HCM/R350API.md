# R350API

## Descrição

S-2240 - eSocial - Condições Ambientais do Trabalho - Atividades (Obsoleta)

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data em que o trabalhador iniciou as atividades no ambiente de trabalho |
| SeqCon | Number(009,0) | Não | Sequência |
| SeqApi | Number(009,0) | Não | Sequência Atividades Periculosas ou Insalubres |
| CodAtv | String(006) | Sim | Código da atividade desempenhada dentre as descritas na Tabela 28 |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatIni
- SeqCon
- SeqApi

---

## Índices

### R350APIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
