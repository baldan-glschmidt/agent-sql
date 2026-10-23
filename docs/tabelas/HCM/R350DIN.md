# R350DIN

## Descrição

S-2299 - eSocial - Dias Trabalhados Intermitente

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
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqDes | Number(009,0) | Não | Sequência |
| SeqDin | Number(009,0) | Não | Sequência |
| DiaMes | Number(002,0) | Sim | Dia do Mês |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| HorTra | String(004) | Sim | Horas Trabalhadas |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqDin

---

## Índices

### R350DINIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
