# R349RRA

## Descrição

S-5002 - eSocial - Informações complementares relativas a RRA

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
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIdv | Number(009,0) | Não | Sequência |
| SeqRra | Number(009,0) | Não | Sequência |
| TipPro | Number(001,0) | Sim | Código Correspondente ao Tipo do Processo |
| NumPro | String(021) | Sim | Número do Processo Administrativo/Judicial |
| DesRra | String(050) | Sim | Descrição dos Rendimentos Recebidos Acumuladamente - RRA |
| MesRra | Number(004,1) | Sim | Número de meses relativo aos Rendimentos Recebidos Acumuladamente - RRA |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIdv
- SeqRra

---

## Índices

### R349RRAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
