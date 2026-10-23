# R044TVE

## Descrição

Tipos de Vales - Faixas do Empregado

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Tipo do Vale |
| VlrFai | Number(011,2) | Não | Valor Teto da Faixa |
| PerCol | Number(005,2) | Sim | Percentual Sobre o Valor do Vale |

---

## Chave Primária

- TabEve
- CodVal
- VlrFai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044TVE_001

**Tabela:** R044TVL

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodVal | CodVal |

