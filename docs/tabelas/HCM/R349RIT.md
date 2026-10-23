# R349RIT

## Descrição

S-5002 - eSocial - Informações relativas ao IRRF (versão 2.5)

---

## Resumo

- Campos: 10
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
| SeqIrc | Number(009,0) | Não | Sequência |
| SeqRit | Number(009,0) | Não | Sequência |
| CodRec | Number(006,0) | Sim | Código de Receita (CR) da contribuição descontada do trabalhador |
| ValDes | Number(014,2) | Sim | Valor da base de cálculo, retenção, dedução ou isenção do IR Retido na Fonte |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIrc
- SeqRit

---

## Índices

### R349RITIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
