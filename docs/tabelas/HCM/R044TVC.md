# R044TVC

## Descrição

Tipos de Vales - Cédulas

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Vale |
| VlrCed | Date | Não | Valor da Cédula |

---

## Chave Primária

- TabEve
- CodVal
- VlrCed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044TVC_001

**Tabela:** R044TVL

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodVal | CodVal |

