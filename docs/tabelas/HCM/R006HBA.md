# R006HBA

## Descrição

Horários da busca automática

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEsc | Number(009,0) | Não | Código de Escala |
| SeqReg | Number(003,0) | Não | Sequência do Registro |
| SeqHOp | Number(003,0) | Não | Sequência do Registro de horário |
| CodHOp | Number(004,0) | Sim | Código do Horário Opcional |

---

## Chave Primária

- CodEsc
- SeqReg
- SeqHOp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R006HBA_000

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

### IR_R006HBA_003

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHOp | CodHor |

