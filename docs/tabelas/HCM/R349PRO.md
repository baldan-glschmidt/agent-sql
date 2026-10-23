# R349PRO

## Descrição

S-5002 - eSocial - Processos - Não retenção de tributos ou depósitos judiciais

---

## Resumo

- Campos: 12
- Chave Primária: 8 campo(s)
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
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqCri | Number(009,0) | Não | Sequência |
| SeqPro | Number(009,0) | Não | Sequência |
| TipPro | Number(001,0) | Sim | Código Correspondente ao Tipo do Processo |
| NumPro | String(020) | Não | Número do Processo Judicial |
| CodSus | Number(014,0) | Sim | Código do indicativo da suspensão, atribuído pelo contribuinte |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqCri
- SeqPro

---

## Índices

### R349PROIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
