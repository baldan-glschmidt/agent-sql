# R146DET

## Descrição

Provisão - Tipos de Valor da Provisão

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| TipVal | Number(002,0) | Não | Tipo de Valor |
| DesVal | String(100) | Sim | Descrição do Valor |
| PerVal | Number(011,2) | Sim | Percentual/Qtd Dias Provisão |
| TipEnc | Number(001,0) | Sim | Indica se o Tipo de Valor é Encargo |
| ArrVal | Number(001,0) | Sim | Arredondamento |
| BasDet | Number(001,0) | Sim | Determina Como Será Montada a Base Deste Valor |
| RegAju | Number(003,0) | Sim | Código da Regra de Ajuste da Base |
| CodTot | Number(004,0) | Sim | Código do Totalizador |

---

## Chave Primária

- TipPrv
- TipVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146DET_000

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

