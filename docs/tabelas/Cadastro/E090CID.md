# E090CID

## Descrição

Cadastros - Representantes - Cidades de Atuação

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRep | Number(009,0) | Não | Código do representante |
| CodRai | Number(007,0) | Não | Código da cidade p/RAIS que o representante não tem cliente |
| SitReg | String(001) | Não | Situação do registro |

---

## Chave Primária

- CodRep
- CodRai

---

## Índices

### E090CIDIndice1

**Tipo:** Não unico

Campos:
- CodRai

---

## Relacionamentos

### IR_E090CID_000

**Tabela:** E090REP

| Origem | Destino |
|--------|---------|
| CodRep | CodRep |

### IR_E090CID_001

**Tabela:** E008RAI

| Origem | Destino |
|--------|---------|
| CodRai | CodRai |

