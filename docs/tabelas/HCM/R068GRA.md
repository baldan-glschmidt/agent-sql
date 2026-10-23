# R068GRA

## Descrição

Dias Refeições Gratuitas

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRft | Number(004,0) | Não | Código do Refeitório |
| DatIni | Date | Não | Data Inicial Refeições com Valores Gratuitos no Refeitório |
| DatFim | Date | Sim | Data Final Refeições com Valores Gratuitos no Refeitório |

---

## Chave Primária

- CodRft
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R068GRA_000

**Tabela:** R068RFT

| Origem | Destino |
|--------|---------|
| CodRft | CodRft |

