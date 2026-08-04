# E030TMB

## Descrição

Tabelas - Bancos - Tabelas de Moeda

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodMoe | String(003) | Não | Código interno da moeda |
| MoeBan | Number(002,0) | Sim | Código da moeda no banco |
| DesBan | String(100) | Sim | Descrição da espécie do título no banco |

---

## Chave Primária

- CodBan
- CodMoe

---

## Índices

### E030TMBIndice1

**Tipo:** Não unico

Campos:
- CodMoe

---

## Relacionamentos

### IR_E030TMB_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E030TMB_001

**Tabela:** E031MOE

| Origem | Destino |
|--------|---------|
| CodMoe | CodMoe |

