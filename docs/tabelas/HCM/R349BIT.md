# R349BIT

## Descrição

S-5002 - eSocial - Bases, deduções, isenções e retenções do IRRF (versão 2.5)

---

## Resumo

- Campos: 11
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
| SeqBit | Number(009,0) | Não | Sequência |
| TipVal | Number(004,0) | Sim | Tipo de valor relativo aos rendimentos pagos e ao IRRF retido |
| ValBas | Number(014,2) | Sim | Valor da base de cálculo, retenção, dedução ou isenção do IR Retido na Fonte |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| DesRen | String(100) | Sim | Descrição do rendimento não tributável ou isento do IRRF |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIrc
- SeqBit

---

## Índices

### R349BITIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
