# R349JUD

## Descrição

S-5002 - eSocial - Informações complementares - Exigibilidade suspensa

---

## Resumo

- Campos: 13
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
| SeqIdv | Number(009,0) | Não | Sequência |
| SeqBdi | Number(009,0) | Não | Sequência |
| SeqJud | Number(009,0) | Não | Sequência |
| NumPro | String(020) | Não | Número do Processo Judicial |
| UfVara | String(002) | Sim | Unidade da Federação - UF da Seção Judiciária |
| CodMun | Number(007,0) | Sim | Código do município, conforme tabela do IBGE |
| IdeVar | String(004) | Sim | Código de identificação da Vara |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIdv
- SeqBdi
- SeqJud

---

## Índices

### R349JUDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
