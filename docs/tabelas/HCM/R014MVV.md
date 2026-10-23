# R014MVV

## Descrição

Parâmetros p/ Média de Valores Variáveis (Obsoleta)

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSin | Number(004,0) | Não | Código do Sindicato |
| TipMed | Number(001,0) | Não | Tipo da Média |
| ForCal | Number(002,0) | Não | Forma de calcular a média de valores variáveis |
| MesPes | Number(002,0) | Sim | Quantidade de meses a pesquisar p/ média |
| MesMed | Number(002,0) | Sim | Qtde de "maiores meses" a utilizar na média |
| MesDiv | Number(002,0) | Sim | Qtde de meses que se dividirá a soma dos valores apurados |
| CorVar | String(001) | Sim | Corrigir Valores Variáveis |

---

## Chave Primária

- CodSin
- TipMed
- ForCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R014MVV_000

**Tabela:** R014SIN

| Origem | Destino |
|--------|---------|
| CodSin | CodSin |

