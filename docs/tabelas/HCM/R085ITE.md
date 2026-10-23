# R085ITE

## Descrição

Orçamento - Itens de Cálculo

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IteOrc | Number(003,0) | Não | Código do Item |
| NomIte | String(040) | Sim | Nome do Item |
| RegCal | Number(002,0) | Sim | Tipo do Item |
| RegEsp | Number(003,0) | Sim | Regra Específica |
| ValCal | Number(013,4) | Sim | Valor de Cálculo |
| MesMed | Number(002,0) | Sim | Meses Média |
| ProDia | String(001) | Sim | Proporcionalidade(S,N) |
| ConPer | Number(001,0) | Sim | O % deve ser informado todo mês ou somente no mês específico |
| ReaIte | String(001) | Sim | Indica se deve aplicar o % de reajuste sobre o ítem(S,N) |
| PorCar | String(001) | Sim | Calcula por cargo/posto, independente de variação do quadro(S,N) |
| ProIte | Number(001,0) | Sim | Proporcionaliza conforme dias do mês |
| RatIte | String(001) | Sim | Identifica se o item deve ratear horas/valores(S,N) |
| IteExt | String(001) | Sim | Item Extinto (S,N) |

---

## Chave Primária

- IteOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
