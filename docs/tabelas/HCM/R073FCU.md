# R073FCU

## Descrição

Fases do Curso

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
| CurAlu | Number(003,0) | Não | Código do Curso |
| CodFas | Number(003,0) | Não | Código da Fase |
| DesFCu | String(050) | Sim | Descrição Detalhada da Fase do Curso |

---

## Chave Primária

- CurAlu
- CodFas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073FCU_000

**Tabela:** R073CUR

| Origem | Destino |
|--------|---------|
| CurAlu | CurAlu |

### IR_R073FCU_001

**Tabela:** R073FAS

| Origem | Destino |
|--------|---------|
| CodFas | CodFas |

