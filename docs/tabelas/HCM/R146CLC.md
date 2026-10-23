# R146CLC

## Descrição

Provisão - CLC's

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| SeqPrv | Number(001,0) | Não | Sequência |
| TipVal | Number(002,0) | Não | Tipo de Valor |
| CodTab | Number(003,0) | Sim | Código Tabela de Eventos |
| BasPrv | Number(004,0) | Sim | CLC da Base Provisão |
| PerVal | Number(004,0) | Sim | CLC de Percentual / Qtd Dias Provisionado |
| SalAnt | Number(004,0) | Sim | CLC do Saldo Anterior |
| SalTrf | Number(004,0) | Sim | CLC do Saldo Transferido |
| AjuPrv | Number(004,0) | Sim | CLC de Ajuste Provisão |
| PrvMes | Number(004,0) | Sim | CLC da Provisão Mensal |
| ValPag | Number(004,0) | Sim | CLC do Valor Pago |
| ValAdt | Number(004,0) | Sim | CLC do Valor 13° Salário Adiantado |
| ValInd | Number(004,0) | Sim | CLC do Valor 13° Salário Indenizado |
| PagMai | Number(004,0) | Sim | CLC do Valor Pago a Maior |
| AjuMai | Number(004,0) | Sim | CLC do Ajuste Pago a Maior |
| SldAtu | Number(004,0) | Sim | CLC do Saldo Atual |

---

## Chave Primária

- TipPrv
- SeqPrv
- TipVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146CLC_000

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

### IR_R146CLC_002

**Tabela:** R146DET

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |
| TipVal | TipVal |

