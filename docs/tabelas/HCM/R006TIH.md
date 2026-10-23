# R006TIH

## Descrição

Turmas de Intervalo - Horários

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEsc | Number(009,0) | Não | Código da Escala |
| TurInt | Number(009,0) | Não | Código da Turma de Intervalo |
| CodHor | Number(004,0) | Não | Código do Horário |
| CodInt | Number(009,0) | Sim | Código do Intervalo |

---

## Chave Primária

- CodEsc
- TurInt
- CodHor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R006TIH_001

**Tabela:** R006TIN

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |
| TurInt | TurInt |

### IR_R006TIH_002

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

### IR_R006TIH_003

**Tabela:** R006INT

| Origem | Destino |
|--------|---------|
| CodInt | CodInt |

