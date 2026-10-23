# R074CID

## Descrição

Cidades

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCid | Number(007,0) | Não | Código da Cidade |
| NomCid | String(030) | Sim | Nome da Cidade |
| EstCid | String(002) | Sim | Estado da Cidade |
| CodPai | Number(004,0) | Sim | Código do País |
| CodEst | String(004) | Sim | Estado da cidade |
| CodMun | String(012) | Sim | Código do Município (IBGE) |
| PerIss | Number(005,2) | Sim | Percentual de ISS |
| DisCid | String(050) | Sim | Distrito |

---

## Chave Primária

- CodCid

---

## Índices

### R074CIDIndice2

**Tipo:** Unico

Campos:
- NomCid
- CodCid

### R074CIDIndice3

**Tipo:** Não unico

Campos:
- CodPai

### R074CIDPaisEstadoCidade

**Tipo:** Unico

Campos:
- CodPai
- CodEst
- CodCid

---

## Relacionamentos

### IR_R074CID_003

**Tabela:** R074PAI

| Origem | Destino |
|--------|---------|
| CodPai | CodPai |

### IR_R074CID_004

**Tabela:** R074EST

| Origem | Destino |
|--------|---------|
| CodPai | CodPai |
| CodEst | CodEst |

