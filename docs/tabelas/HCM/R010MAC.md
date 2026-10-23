# R010MAC

## Descrição

Motivo da Situação para Acerto

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSit | Number(003,0) | Não | Código da Situação |
| MotSit | Number(003,0) | Não | Motivo da Situação |

---

## Chave Primária

- CodSit
- MotSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010MAC_000

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

### IR_R010MAC_001

**Tabela:** R010MOT

| Origem | Destino |
|--------|---------|
| MotSit | MotSit |

