# E035REL

## Descrição

Tabelas - Relacionamento de instruções

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 2
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodOct | String(003) | Não | Código interno de ocorrência de retorno |
| OctBan | String(003) | Não | Código de ocorrência de retorno no banco |
| CodOcr | String(003) | Não | Código interno de ocorrência de remessa |

---

## Chave Primária

- CodBan
- CodOct
- OctBan

---

## Índices

### E035RELIndice1

**Tipo:** Não unico

Campos:
- CodOct

### E035RELIndice2

**Tipo:** Não unico

Campos:
- CodBan
- CodOcr

---

## Relacionamentos

### IR_E035REL_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E035REL_001

**Tabela:** E035OCT

| Origem | Destino |
|--------|---------|
| CodOct | CodOct |

### IR_E035REL_002

**Tabela:** E030ORT

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |
| CodOct | CodOct |
| OctBan | OctBan |

### IR_E035REL_003

**Tabela:** E030ORM

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |
| CodOcr | CodOcr |

