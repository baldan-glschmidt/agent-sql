# R074RAD

## Descrição

Regiões Administrativas

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
| CodCid | Number(007,0) | Não | Código da Cidade |
| CodRad | Number(002,0) | Não | Código da Região Administrativa |
| NomRad | String(040) | Sim | Nome da Região Administrativa |

---

## Chave Primária

- CodCid
- CodRad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R074RAD_000

**Tabela:** R074CID

| Origem | Destino |
|--------|---------|
| CodCid | CodCid |

