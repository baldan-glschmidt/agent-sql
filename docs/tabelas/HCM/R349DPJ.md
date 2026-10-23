# R349DPJ

## Descrição

S-5002 - eSocial - Detalhamento das despesas com processo judicial - RRA

---

## Resumo

- Campos: 11
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
| SeqRra | Number(009,0) | Não | Sequência |
| SeqDpj | Number(009,0) | Não | Sequência |
| VlrCus | Number(014,2) | Sim | Valor das despesas com custas judiciais - RRA |
| VlrAdv | Number(014,2) | Sim | Valor total das despesas com advogado(s) - RRA |
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
- SeqDpj

---

## Índices

### R349DPJIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
