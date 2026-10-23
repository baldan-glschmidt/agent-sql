# R014MED

## Descrição

Parâmetros p/ Médias

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| OriMed | Number(002,0) | Não | Origem dos Valores para Cálculo de Média |
| TipMed | Number(001,0) | Não | Tipo da Média |
| ForCal | Number(002,0) | Não | Forma de Calcular a Média de Valores |
| MesPes | Number(002,0) | Sim | Qtde de Meses a Pesquisar p/ Média |
| MesMed | Number(002,0) | Sim | Qtde de "Maiores Meses" a Utilizar na Média |
| MesDiv | Number(002,0) | Sim | Qtde de Meses que se Dividirá a Soma dos Valores Apurados |
| MesVal | Number(002,0) | Sim | Qtde mínima de meses com valor para que o sistema calcule a média |
| CorVar | String(001) | Sim | Corrigir Valores |
| MedRcs | Number(001,0) | Sim | Definir como será feita a contagem dos meses para médias na rescisão |

---

## Chave Primária

- CodSin
- OriMed
- TipMed
- ForCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014MED_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

