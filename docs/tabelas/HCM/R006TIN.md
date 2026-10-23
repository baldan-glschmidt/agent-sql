# R006TIN

## Descrição

Turmas de Intervalo

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEsc | Number(009,0) | Não | Código da Escala |
| TurInt | Number(009,0) | Não | Código da Turma de Intervalo |
| DesTIn | String(030) | Sim | Descrição da Turma de Intervalo |
| DesSim | String(999) | Sim | Descrição da jornada para o eSocial Simplificado |

---

## Chave Primária

- CodEsc
- TurInt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R006TIN_000

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

