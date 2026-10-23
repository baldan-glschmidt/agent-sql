# R349PLD

## Descrição

S-5002 - eSocial - Informações de dependente de plano de saúde

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
| SeqCpl | Number(009,0) | Não | Sequência |
| SeqPln | Number(009,0) | Não | Sequência |
| SeqPld | Number(009,0) | Não | Sequência |
| NumCpf | Number(011,0) | Sim | Número do CPF do dependente do plano de saúde |
| VlrDed | Number(014,2) | Sim | Valor relativo a dedução do rendimento tributável correspondente a pagamento a plano de saúde do dependente |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl
- SeqPln
- SeqPld

---

## Índices

### R349PLDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
