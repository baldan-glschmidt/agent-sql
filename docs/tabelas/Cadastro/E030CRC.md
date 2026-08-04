# E030CRC

## Descrição

Tabelas - Bancos - Carteiras de Cobrança

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
| CodCrt | String(002) | Não | Código interno da carteira de cobrança |
| CrtBan | String(003) | Sim | Código da carteira de cobrança no banco |
| DesBan | String(100) | Sim | Descrição da carteira de cobrança no banco |
| CodCrb | String(001) | Sim | Código da carteira no banco |
| VarCrc | String(003) | Sim | Variação da carteira de cobrança |

---

## Chave Primária

- CodBan
- CodCrt

---

## Índices

### E030CRCIndice1

**Tipo:** Não unico

Campos:
- CodCrt

---

## Relacionamentos

### IR_E030CRC_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E030CRC_001

**Tabela:** E033CRT

| Origem | Destino |
|--------|---------|
| CodCrt | CodCrt |

