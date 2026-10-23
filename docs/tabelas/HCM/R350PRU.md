# R350PRU

## Descrição

S-1010 - eSocial - Processos da Tabela de Rubricas

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| RubEso | String(030) | Não | Código da rubrica eSocial |
| SeqRub | Number(009,0) | Não | Sequência |
| IdePro | Number(001,0) | Não | Identificação do Processo da Rubrica: INSS, IRRF, FGTS ou Contrib. Sindical |
| SeqPro | Number(002,0) | Não | Sequência Processo |
| NumPro | String(021) | Sim | Núm. processo que determina não incidência de INSS, IRRF, FGTS ou Cont. Sindical |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| TipPro | Number(001,0) | Sim | Tipo do processo que determina a não incidência de contribuição previdenciária |
| DePrLr | Number(001,0) | Sim | Decisão do processo que determina não incidência de contribuição previdenciária |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |

---

## Chave Primária

- NumEmp
- FilEmp
- RubEso
- SeqRub
- IdePro
- SeqPro

---

## Índices

### R350PRUIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
