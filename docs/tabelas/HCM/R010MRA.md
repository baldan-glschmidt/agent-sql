# R010MRA

## Descrição

Situações - Movimento Rais

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
| CodSit | Number(003,0) | Não | Código da Situação |
| CmpMov | Date | Não | Competência do Movimento |
| MovRai | Number(002,0) | Sim | Código de Movimento da Rais |

---

## Chave Primária

- CodSit
- CmpMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010MRA_000

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

