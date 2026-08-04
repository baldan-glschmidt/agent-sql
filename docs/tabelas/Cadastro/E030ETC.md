# E030ETC

## Descrição

Tabelas - Bancos - Espécies de Título

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
| CodTpt | String(003) | Não | Código de Tipo de Título |
| EspBan | String(003) | Sim | Código da espécie do título no banco |
| DesBan | String(100) | Sim | Descrição da espécie do título no banco |

---

## Chave Primária

- CodBan
- CodTpt

---

## Índices

### E030ETCIndice1

**Tipo:** Não unico

Campos:
- CodTpt

---

## Relacionamentos

### IR_E030ETC_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E030ETC_001

**Tabela:** E002TPT

| Origem | Destino |
|--------|---------|
| CodTpt | CodTpt |

