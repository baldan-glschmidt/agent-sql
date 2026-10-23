# R350INT

## Descrição

S-1050 - eSocial - Horários do Intervalo

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| HorEso | String(030) | Não | Código atribuído pelo empresa para o Horário Contratual |
| SeqHor | Number(009,0) | Não | Sequência |
| SeqInt | Number(009,0) | Não | Sequência |
| IdeInt | Number(009,0) | Sim | Identificador |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodHor | Number(004,0) | Sim | Código do Horário |
| TipInt | Number(001,0) | Sim | Tipo Intervalo |
| DurInt | Number(004,0) | Sim | Tempo de duração do intervalo, em minutos |
| IniInt | Number(004,0) | Sim | Hora de início do intevalo |
| FimInt | Number(004,0) | Sim | Hora de termino do intervalo |
| VarEnt | Number(003,0) | Sim | Variação em minutos possível na hora de saída do trabalhador |
| VarSai | Number(003,0) | Sim | Variação em minutos possível na hora de saída do trabalhador |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| LayOut | String(006) | Sim | Leiaute |

---

## Chave Primária

- NumEmp
- FilEmp
- HorEso
- SeqHor
- SeqInt

---

## Índices

### R350INTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
