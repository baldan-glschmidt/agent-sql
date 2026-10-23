# R349ADV

## Descrição

S-5002 - eSocial - Identificação dos advogados - RRA

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
| SeqRra | Number(009,0) | Não | Sequência |
| SeqAdv | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do advogado |
| CfjIns | String(014) | Sim | Número de inscrição do advogado |
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
- SeqAdv

---

## Índices

### R349ADVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
