# R011PBH

## Descrição

Período do Banco de Horas

---

## Resumo

- Campos: 25
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBhr | Number(005,0) | Não | Código do Banco de Horas |
| DatIni | Date | Não | Início do Período |
| DatFim | Date | Sim | Fim do Período |
| FecDia | Number(001,0) | Sim | Fechamento do Dia |
| FSeEsc | String(001) | Sim | Fechamento pela Escala |
| FecMes | String(001) | Sim | Fechamento do Mês |
| DiaMes | Number(002,0) | Sim | Dia do Mês para Fechamento Mensal |
| TemLiC | String(001) | Sim | Tem Limite Crédito |
| TemLiD | String(001) | Sim | Tem Limite Débito |
| TipLiC | String(001) | Sim | Tipo Limite de Crédito |
| TipLiD | String(001) | Sim | Tipo Limite de Débito |
| TpoLiC | Number(003,0) | Sim | Tempo Limite de Crédito |
| TpoLiD | Number(003,0) | Sim | Tempo Limite de Débito |
| FecCre | String(001) | Sim | Fechamento Crédito |
| FecDeb | String(001) | Sim | Fechamento Débito |
| LiCDia | Number(010,0) | Sim | Limite de Crédito Diário do Banco |
| LiCDFo | Number(010,0) | Sim | Limite de Crédito Diário do Banco em Dias de Folga |
| LiCDTo | Number(010,0) | Sim | Limite de Crédito Diário Banco (Trabalho e Extras) |
| LiCSem | Number(010,0) | Sim | Limite de Crédito Semanal do Banco |
| LiCMes | Number(010,0) | Sim | Limite de Crédito Mensal do Banco |
| LiCPer | Number(010,0) | Sim | Limite de Saldo de Crédito Período |
| LiDDia | Number(010,0) | Sim | Limite de Débito Diário do Banco |
| LiDSem | Number(010,0) | Sim | Limite de Débito Semanal do Banco |
| LiDMes | Number(010,0) | Sim | Limite de Débito Mensal do Banco |
| LiDPer | Number(010,0) | Sim | Limite de Saldo de Débito Período |

---

## Chave Primária

- CodBhr
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011PBH_000

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBhr | CodBHr |

