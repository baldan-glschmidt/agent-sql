# R350CCR

## Descrição

S-1210 - eSocial - Informações relativas a planos de previdência complementar

---

## Resumo

- Campos: 16
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| SeqPrt | Number(009,0) | Não | Sequência |
| SeqInf | Number(009,0) | Não | Sequência |
| SeqRcr | Number(009,0) | Não | Sequência |
| SeqCcr | Number(009,0) | Não | Sequência |
| TipPre | Number(001,0) | Sim | Tipo de previdência complementar |
| CnpjEn | Number(014,0) | Sim | Número de inscrição da entidade de previdência complementar |
| CfjIns | String(014) | Sim | Número de inscrição da entidade de previdência complementar |
| VlrDed | Number(014,2) | Sim | Valor da dedução relativa à previdência complementar |
| VlrD13 | Number(014,2) | Sim | Valor da dedução do 13º Salário relativa à previdência complementar |
| VlrPat | Number(014,2) | Sim | Valor da contribuição do ente público patrocinador da Funpresp |
| VlrP13 | Number(014,2) | Sim | Valor da contribuição do 13º Salário do ente público patrocinador da Funpresp |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt
- SeqInf
- SeqRcr
- SeqCcr

---

## Índices

### R350CCRIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
