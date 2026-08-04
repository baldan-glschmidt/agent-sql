# E030TBB

## Descrição

Tabelas - Bancos - Tarifas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodTrb | String(003) | Não | Código interno da tarifa bancária |
| TrbBan | String(003) | Não | Código da tarifa no banco |
| DesTbb | String(040) | Sim | Descrição da tarifa no banco |
| VlrTbb | Number(015,2) | Sim | Valor do tarifa no banco |

---

## Chave Primária

- CodBan
- CodTrb
- TrbBan

---

## Índices

### E030TBBIndice1

**Tipo:** Não unico

Campos:
- CodTrb

---

## Relacionamentos

### IR_E030TBB_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E030TBB_001

**Tabela:** E030TRB

| Origem | Destino |
|--------|---------|
| CodTrb | CodTrb |

