# R026ICM

## Descrição

Índices de conversão de moedas

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMoe | String(003) | Não | Código da moeda de origem |
| MoeDes | String(003) | Não | Código da moeda de destino |
| CodIdm | Number(003,0) | Sim | Índice de conversão |

---

## Chave Primária

- CodMoe
- MoeDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026ICM_000

**Tabela:** R026MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

### IR_R026ICM_001

**Tabela:** R026MOE

| Origem | Destino |
|--------|---------|
| MoeDes | CodMoe |

### IR_R026ICM_002

**Tabela:** R026IDM

| Origem | Destino |
|--------|---------|
| CodIdm | CodIdm |

