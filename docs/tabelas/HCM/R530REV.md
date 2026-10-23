# R530REV

## Descrição

Grupo de Requisitos - Revisão

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruReq | String(010) | Não | Código do grupo de requisitos |
| RevGRq | String(010) | Não | Identificador da revisão do grupo de requisitos |
| DatIni | Date | Sim | Determina o início da validade da revisão do grupo de requisitos |
| DatTer | Date | Sim | Determina o término da validade da revisão do grupo de requisitos |
| AnoRev | String(2000) | Sim | Anotações da revisão do grupo de requisitos |

---

## Chave Primária

- GruReq
- RevGRq

---

## Índices

### R530REVIndice1

**Tipo:** Unico

Campos:
- GruReq
- RevGRq
- DatIni

---

## Relacionamentos

### IR_R530REV_000

**Tabela:** R530GRQ

| Origem | Destino |
|--------|---------|
| GruReq | GruReq |

