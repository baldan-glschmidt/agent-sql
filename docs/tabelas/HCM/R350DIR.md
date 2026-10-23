# R350DIR

## Descrição

S-2299 - eSocial - Rubricas que compõe a remuneração do trabalhador nos períodos de apuração anteriores

---

## Resumo

- Campos: 18
- Chave Primária: 10 campo(s)
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
| SeqRec | Number(009,0) | Não | Sequência |
| SeqDis | Number(009,0) | Não | Sequência |
| SeqDpr | Number(009,0) | Não | Sequência |
| SeqDil | Number(009,0) | Não | Sequência |
| SeqDir | Number(009,0) | Não | Sequência |
| CodRub | String(030) | Sim | Código que identifica a rubrica na folha de pagamento |
| TabRub | String(008) | Sim | Tabela de Rubrica |
| QtdRef | Number(006,2) | Sim | Quantidade de referência para apuração |
| FatRub | Number(005,2) | Sim | Fator, percentual, etc, da rubrica |
| ValUni | Number(014,2) | Sim | Valor unitário da rubrica |
| ValRub | Number(014,2) | Sim | Valor da rubrica |
| ApuIrf | Number(001,0) | Sim | Indicativo de tipo de apuração de IR |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqRec
- SeqDis
- SeqDpr
- SeqDil
- SeqDir

---

## Índices

### R350DIRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
