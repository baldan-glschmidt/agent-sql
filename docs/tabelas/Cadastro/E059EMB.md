# E059EMB

## Descrição

Tabelas - Tipos de Embalagens

---

## Resumo

- Campos: 19
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmb | Number(004,0) | Não | Código da embalagem |
| DesEmb | String(030) | Não | Descrição da embalagem |
| AbrEmb | String(015) | Não | Abreviatura da embalagem |
| LarEmb | Number(009,3) | Sim | Largura da embalagem |
| ComEmb | Number(009,3) | Sim | Comprimento da embalagem |
| AltEmb | Number(009,3) | Sim | Altura da embalagem |
| PesEmb | Number(011,5) | Sim | Peso da embalagem |
| CodAge | String(010) | Sim | Não Utilizar - Será excluído |
| EmbExp | String(001) | Sim | Indicativo se a embalagem pode ser utilizada para expedição ou é somente para estocagem |
| CodAem | String(010) | Sim | Código do agrupamento para embalagens |
| PrfEmb | Number(009,3) | Sim | Profundidade da Embalagem |
| CpdEmp | Number(004,0) | Sim | Capacidade de Empilhamento |
| UniPes | String(003) | Sim | Código da unidade de medida do peso da embalagem |
| UniDim | String(003) | Sim | Código da unidade de medida para as dimensões da embalagem |
| DmtEmb | Number(009,3) | Sim | Diâmetro da embalagem |
| EmbPri | String(001) | Sim | Indicativo se a embalagem é primária (contato com os produtos) |
| CodBar | Number(013,0) | Sim | Código de barras EAN13 |
| CodBa2 | String(030) | Sim | Código de barras livre |
| CatEmb | String(003) | Sim | Categoria da embalagem |

---

## Chave Primária

- CodEmb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
