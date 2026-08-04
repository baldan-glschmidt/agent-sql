# E030ORM

## Descrição

Tabelas - Bancos - Ocorrências de Remessa

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodOcr | String(003) | Não | Código interno de ocorrência de remessa |
| OcrBan | String(003) | Sim | Código de ocorrência de remessa no banco |
| DesBan | String(100) | Sim | Descrição da ocorrência de remessa no banco |
| CodIn1 | String(003) | Sim | Código da 1º Instrução da ocorrência |
| CodIn2 | String(003) | Sim | Código da 2º Instrução da ocorrência |

---

## Chave Primária

- CodBan
- CodOcr

---

## Índices

### E030ORMIndice1

**Tipo:** Não unico

Campos:
- CodOcr

---

## Relacionamentos

### IR_E030ORM_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E030ORM_001

**Tabela:** E035OCR

| Origem | Destino |
|--------|---------|
| CodOcr | CodOcr |

