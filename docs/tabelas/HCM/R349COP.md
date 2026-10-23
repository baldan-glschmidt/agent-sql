# R349COP

## Descrição

S-5011 - eSocial - Informações de substituição prevista na Lei 12.546/2011

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
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCeo | Number(009,0) | Não | Sequência |
| SeqCle | Number(009,0) | Não | Sequência |
| SeqCop | Number(009,0) | Não | Sequência |
| OpCnpj | Number(014,0) | Sim | CNPJ do Operador Portuário |
| CfjIns | String(014) | Sim | CNPJ do Operador Portuário |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo
- SeqCle
- SeqCop

---

## Índices

### R349COPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
