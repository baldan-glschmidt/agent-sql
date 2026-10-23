# R999GRF

## Descrição

Campos das grids personalizadas pelo usuário

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodUsu | Number(010,0) | Não | Código do usuário |
| ModId | Number(005,0) | Não | Módulo |
| NomFrm | String(030) | Não | Nome Form |
| NomGri | String(030) | Não | Nome Grid |
| FldNam | String(050) | Não | Nome do campo |
| WIDTH | Number(005,0) | Sim | Tamanho do campo |
| IndFld | Number(005,0) | Sim | Posição do campo na grid |
| KidOrd | Number(005,0) | Sim | Tipo de ordenação |

---

## Chave Primária

- CodUsu
- ModId
- NomFrm
- NomGri
- FldNam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R999GRF_003

**Tabela:** R999GRI

| Origem | Destino |
|--------|---------|
| CodUsu | CodUsu |
| ModId | ModId |
| NomFrm | NomFrm |
| NomGri | NomGri |

