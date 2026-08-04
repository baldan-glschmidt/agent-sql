# E030ORP

## Descrição

Tabelas - Bancos - Ocorrências de Retorno do PE (Pagamento Eletrônico)

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodBan | String(003) | Não | Código do banco na Febraban |
| CodOct | String(003) | Não | Código interno de ocorrência de retorno |
| OctBan | String(003) | Não | Código de ocorrência de retorno no banco |
| DesBan | String(100) | Sim | Descrição da ocorrência de retorno no banco |

---

## Chave Primária

- CodBan
- CodOct
- OctBan

---

## Índices

### E030ORPIndice1

**Tipo:** Não unico

Campos:
- CodOct

---

## Relacionamentos

### IR_E030ORP_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E030ORP_001

**Tabela:** E035OPE

| Origem | Destino |
|--------|---------|
| CodOct | CodOct |

