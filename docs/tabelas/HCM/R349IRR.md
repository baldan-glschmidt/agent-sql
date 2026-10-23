# R349IRR

## Descrição

S-5012 - eSocial - Informações consolidadas do IRRF por código de Receita

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| TipFol | Number(001,0) | Não | Tipo Folha |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqIrr | Number(009,0) | Não | Sequência |
| CodRec | Number(006,0) | Sim | Código de Receita - CR relativo ao Imposto de Renda Retido na Fonte |
| ValRec | Number(014,2) | Sim | Valor correspondente ao Código de Receita apurado |
| ValSus | Number(014,2) | Sim | Valor com Exigibilidade Suspensa correspondente ao Código de Receita |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- TipFol
- SeqTab
- SeqIrr

---

## Índices

### R349IRRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
