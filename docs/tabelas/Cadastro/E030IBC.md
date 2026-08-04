# E030IBC

## Descrição

Tabelas - Bancos - Instruções Bancárias

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
| CodIns | String(003) | Não | Código interno da instrução bancária |
| InsBan | String(003) | Sim | Código da Instrução no Banco |
| DesBan | String(100) | Sim | Descrição da instrução no Banco |

---

## Chave Primária

- CodBan
- CodIns

---

## Índices

### E030IBCIndice1

**Tipo:** Não unico

Campos:
- CodIns

---

## Relacionamentos

### IR_E030IBC_000

**Tabela:** E030BAN

| Origem | Destino |
|--------|---------|
| CodBan | CodBan |

### IR_E030IBC_001

**Tabela:** E036INS

| Origem | Destino |
|--------|---------|
| CodIns | CodIns |

