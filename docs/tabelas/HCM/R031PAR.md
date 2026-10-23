# R031PAR

## Descrição

Geração de Escalas - Parâmetros Por Competência

---

## Resumo

- Campos: 18
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEqp | Number(004,0) | Não | Código da Equipe |
| CodTur | Number(001,0) | Não | Código do Turno |
| CodCat | Number(003,0) | Não | Código da Categoria |
| DatCmp | Date | Não | Data Competência |
| QtdFPM | Number(002,0) | Sim | Quantidade de Folgas Previstas no Mês |
| QtdTPM | Number(002,0) | Sim | Quantidade de Trabalhos Previstos no Mês |
| MinFSF | Number(002,0) | Sim | Número Mínimo de Finais de Semana de Folga |
| MinDFo | Number(002,0) | Sim | Número Mínimo de Domingos de Folga |
| MinFFe | Number(002,0) | Sim | Número Mínimo de Folgas em Feriados |
| MaxDCT | Number(002,0) | Sim | Número Máximo de Dias Consecutivos de Trabalho |
| MinDCT | Number(002,0) | Sim | Número Mínimo de Dias Consecutivos de Trabalho |
| MaxDCF | Number(002,0) | Sim | Número Máximo de Dias Consecutivos de Folga |
| MinDCF | Number(002,0) | Sim | Número Mínimo de Dias Consecutivos de Folga |
| MaxPCo | Number(002,0) | Sim | Máximo de Preferências Por Colaborador |
| MinPAC | Number(002,0) | Sim | Mínimo de Preferências Atendidas Por Colaborador |
| QtdCDU | Number(003,0) | Sim | Quantidade Desejada Colaboradores Por Dia Útil |
| QtdCFS | Number(003,0) | Sim | Quantidade Desejada Colaboradores Finais Semana |
| QtdCoQ | Number(003,0) | Sim | Quantidade de Colaboradores no Quadro |

---

## Chave Primária

- CodEqp
- CodTur
- CodCat
- DatCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R031PAR_000

**Tabela:** R031EQP

| Origem | Destino |
|--------|---------|
| CodEqp | CodEqp |

### IR_R031PAR_002

**Tabela:** R031CAT

| Origem | Destino |
|--------|---------|
| CodCat | CodCat |

