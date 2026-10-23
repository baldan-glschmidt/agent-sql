# R400CAM

## Descrição

Campos Não Replicados das Tabelas

---

## Resumo

- Campos: 2
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomTab | String(010) | Não | Nome da Tabela |
| NomCam | String(010) | Não | Nome do Campo da Tabela |

---

## Chave Primária

- NomTab
- NomCam

---

## Índices

### R400CAMIndice2

**Tipo:** Não unico

Campos:
- NomCam

---

## Relacionamentos

### IR_R400CAM_000

**Tabela:** R400TAB

| Origem | Destino |
|--------|---------|
| NomTab | NomTab |

