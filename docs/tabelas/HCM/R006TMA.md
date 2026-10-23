# R006TMA

## Descrição

Turmas da Escala

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEsc | Number(009,0) | Não | Código da escala |
| CodTma | Number(001,0) | Não | Código da Turma |
| DesSim | String(999) | Sim | Descrição da jornada para o eSocial Simplificado |
| TipJoS | Number(002,0) | Sim | Tipo de jornada para o eSocial Simplificado |
| DatBas | Date | Sim | Data Base da Turma |

---

## Chave Primária

- CodEsc
- CodTma

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R006TMA_000

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

