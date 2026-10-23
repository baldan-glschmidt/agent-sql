# R234IAP

## Descrição

Evento - Itens de Avaliação dos Participantes

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEvn | Number(009,0) | Não | Código do Evento |
| CodTnt | Number(003,0) | Não | Item de Nota do Curso |
| SeqEvn | Number(003,0) | Sim | Sequência para avaliação |
| PesNot | Number(002,0) | Sim | Peso da Nota do Curso |

---

## Chave Primária

- CodEvn
- CodTnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234IAP_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

### IR_R234IAP_001

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

