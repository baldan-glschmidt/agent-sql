# E047NTG

## Descrição

Tabelas - Naturezas de Gasto

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodNtg | Number(004,0) | Não | Natureza de Gasto do custo ou despesa |
| DesNtg | String(040) | Não | Descrição da natureza de gasto |
| CodGng | Number(002,0) | Não | Grupo de Natureza de Gasto |
| ForVal | Number(001,0) | Não | Forma de Cálculo de Valor à Vista |
| PrzPgt | Number(003,0) | Sim | Dia Fixo / Prazo de Pagamento |
| TipNtg | String(001) | Não | Tipo de natureza de gasto (Normal / Transferência / Recebimento) |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRdv | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| DesFix | String(001) | Sim | Indicativo se natureza compõe as despesas fixas |

---

## Chave Primária

- CodEmp
- CodNtg

---

## Índices

### E047NTGIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodGng

---

## Relacionamentos

### IR_E047NTG_003

**Tabela:** E047GNG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodGng | CodGng |

