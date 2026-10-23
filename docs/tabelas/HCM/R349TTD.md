# R349TTD

## Descrição

S-5002 - eSocial - Totalizador de tributos com período de apuração diário

---

## Resumo

- Campos: 15
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
| SeqTtd | Number(009,0) | Não | Sequência |
| DiaApu | Number(002,0) | Não | Período de apuração diário do Código de Receita - CR |
| CRIrRt | Number(006,0) | Sim | Código de Receita - CR relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho pagos a residente no exterior para fins fiscais |
| VlIrRt | Number(014,2) | Sim | Valor relativo ao Imposto de Renda Retido na Fonte sobre rendimentos do trabalho pagos a residente, para fins fiscais, no exterior |
| SuIrRt | Number(014,2) | Sim | Valor que deixou de ser descontado do trabalhador relativo ao Imposto de Renda sobre rendimentos do trabalho pagos a residente, para fins fiscais, no exterior |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| FrmTri | Number(002,0) | Sim | Forma de Tributação |
| PaiExt | String(003) | Sim | Código do país de residência para fins fiscais, quando no exterior |
| VlrDia | Number(014,2) | Sim | Valor pago a residente ou domiciliado no exterior |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqIdv
- SeqTtd

---

## Índices

### R349TTDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
