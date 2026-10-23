# R110SUM

## Descrição

Subnormalidade - Medicamentos

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSun | Number(006,0) | Não | Código da subnormalidade |
| CodCon | Number(002,0) | Não | Código da tabela de controle do nível de atenção |
| NivAte | Number(002,0) | Não | Código do nível de atenção |
| CodRem | Number(006,0) | Não | Código do Medicamento |

---

## Chave Primária

- CodSun
- CodCon
- NivAte
- CodRem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110SUM_000

**Tabela:** R110SUN

| Origem | Destino |
|--------|---------|
| CodSun | CodSun |

### IR_R110SUM_003

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

