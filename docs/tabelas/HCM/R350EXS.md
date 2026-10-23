# R350EXS

## Descrição

S-1210 - eSocial - Detalhamento das deduções com exigibilidade suspensa

---

## Resumo

- Campos: 16
- Chave Primária: 10 campo(s)
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
| SeqJcr | Number(009,0) | Não | Sequência |
| SeqVpj | Number(009,0) | Não | Sequência |
| SeqExs | Number(009,0) | Não | Sequência |
| TipDed | Number(001,0) | Sim | Indicativo do tipo de dedução |
| VlrDed | Number(014,2) | Sim | Valor da dedução da base de cálculo do imposto de renda com exigibilidade suspensa |
| CnpjEn | Number(014,0) | Sim | Número de inscrição da entidade de previdência complementar |
| CfjIns | String(014) | Sim | Número de inscrição da entidade de previdência complementar |
| VlrPat | Number(014,2) | Sim | Valor da contribuição do ente público patrocinador da Fundação de Previdência Complementar do Servidor Público (Funpresp) |
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
- SeqJcr
- SeqVpj
- SeqExs

---

## Índices

### R350EXSIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
