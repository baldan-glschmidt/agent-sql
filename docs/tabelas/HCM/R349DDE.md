# R349DDE

## Descrição

S-5002 - eSocial - Dedução do rendimento tributável relativa a dependentes

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
| SeqDde | Number(009,0) | Não | Sequência |
| TipRen | Number(002,0) | Sim | Tipo de rendimento |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| VlrDed | Number(014,2) | Sim | Valor da Dedução da Base de Cálculo |
| Pidexc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqCri
- SeqDde

---

## Índices

### R349DDEIndice1

**Tipo:** Não unico

Campos:
- Pidexc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
