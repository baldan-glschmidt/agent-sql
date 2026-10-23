# R130CUI

## Descrição

Custos do Orçamento  - Item de Custo

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso |
| CmpRea | Date | Não | Competência de Realização |
| SeqTcu | Number(002,0) | Não | Sequência Reserva |
| CodTcu | Number(004,0) | Não | Código do Item de Custo |
| ValCus | Number(011,2) | Sim | Valor do Custo |

---

## Chave Primária

- CodCua
- CmpRea
- SeqTcu
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130CUI_002

**Tabela:** R130CUS

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| CmpRea | CmpCus |
| SeqTcu | SeqCus |

### IR_R130CUI_003

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

