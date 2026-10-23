# R349DSU

## Descrição

S-5002 - eSocial - Detalhamento das deduções com exigibilidade suspensa

---

## Resumo

- Campos: 16
- Chave Primária: 10 campo(s)
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
| SeqRtr | Number(009,0) | Não | Sequência |
| SeqDsu | Number(009,0) | Não | Sequência |
| IndDed | Number(001,0) | Sim | Indicativo do Tipo de Dedução |
| VlrDed | Number(014,2) | Sim | Valor da dedução da base de cálculo do imposto de renda com exigibilidade suspensa |
| NUMPRV | Number(014,0) | Sim | CNPJ da Entidade de Previdência Complementar |
| CfjIns | String(014) | Sim | CNPJ da Entidade de Previdência Complementar |
| VLRPTR | Number(014,2) | Sim | Valor da contribuição do ente público patrocinador da Fundação de Previdência Complementar do Servidor Público (Funpresp) |
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
- SeqRtr
- SeqDsu

---

## Índices

### R349DSUIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
