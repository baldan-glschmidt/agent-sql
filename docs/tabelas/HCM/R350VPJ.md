# R350VPJ

## Descrição

S-1210 - eSocial - Valores - não retenção de tributos ou a depósitos judiciais

---

## Resumo

- Campos: 16
- Chave Primária: 9 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqRcr | Number(009,0) | Não | Sequência |
| SeqJcr | Number(009,0) | Não | Sequência |
| SeqVpj | Number(009,0) | Não | Sequência |
| InApVl | Number(001,0) | Sim | Indicativo de período de apuração |
| VlrNre | Number(014,2) | Sim | Valor da retenção que deixou de ser efetuada em função de processo administrativo ou judicial |
| VlrDep | Number(014,2) | Sim | Valor do depósito judicial em função de processo administrativo ou judicial |
| VlrAtu | Number(014,2) | Sim | Valor da compensação relativa ao ano calendário em função de processo judicial |
| VlrAnt | Number(014,2) | Sim | Valor da compensação relativa a anos anteriores em função de processo judicial |
| VlrSus | Number(014,2) | Sim | Valor do rendimento com exigibilidade suspensa |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqRcr
- SeqJcr
- SeqVpj

---

## Índices

### R350VPJIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
