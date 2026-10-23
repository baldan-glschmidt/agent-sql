# R349EXT

## Descrição

S-5002 - eSocial - Informações complementares relativas a pagamentos no exterior

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
| SeqExt | Number(009,0) | Não | Sequência |
| CodPai | String(003) | Sim | Código do país |
| IndNif | Number(001,0) | Sim | Indicativo do Número de Identificação Fiscal (NIF) |
| NumNif | String(030) | Sim | Número de Identificação Fiscal (NIF) |
| ForTri | Number(002,0) | Sim | Forma de Tributação |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIdv
- SeqExt

---

## Índices

### R349EXTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
