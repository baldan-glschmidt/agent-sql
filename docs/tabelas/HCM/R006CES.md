# R006CES

## Descrição

Escalas Definidas

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEsc | Number(009,0) | Não | Código da Escala Definida |
| DatEsc | Date | Não | Data do Horário da Escala |
| CodHor | Number(004,0) | Sim | Código do Horário |

---

## Chave Primária

- CodEsc
- DatEsc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R006CES_000

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

### IR_R006CES_002

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

