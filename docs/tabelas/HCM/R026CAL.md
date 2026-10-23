# R026CAL

## Descrição

Classes Alíquotas

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAli | Number(002,0) | Não | Código da Alíquota |
| CodCla | Number(002,0) | Não | Código da Classe |
| FilIni | Number(004,0) | Sim | N.de Meses de Filiação Inicial |
| FilFim | Number(004,0) | Sim | N. de Meses de Filiação Final |
| MesInt | Number(002,0) | Sim | Quantidade de Meses Interstício |
| TipIni | String(001) | Sim | Tipo Infor. Inicial (C,M) |
| QtdIni | Number(002,0) | Sim | Qtde Inicial Cfe.Tipo Inicial |
| TipFim | String(001) | Sim | Tipo Informação Final (C,M) |
| QtdFim | Number(002,0) | Sim | Qtde Final Cfe.Tipo Final |
| PerAli | Number(004,2) | Sim | Percentual Alíquota |

---

## Chave Primária

- CodAli
- CodCla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026CAL_000

**Tabela:** R026ALI

| Origem | Destino |
|--------|---------|
| CodAli | CodAli |

