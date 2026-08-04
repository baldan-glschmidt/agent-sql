# E085AIC

## Descrição

Cadastros - Clientes - Áreas de Interesse

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
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodAri | String(003) | Não | Código da área de interesse  do cliente |
| ObsAic | String(030) | Sim | Observações da área de interesse do cliente |

---

## Chave Primária

- CodCli
- CodAri

---

## Índices

### E085AICIndice1

**Tipo:** Não unico

Campos:
- CodAri

---

## Relacionamentos

### IR_E085AIC_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085AIC_001

**Tabela:** E061ARI

| Origem | Destino |
|--------|---------|
| CodAri | CodAri |

