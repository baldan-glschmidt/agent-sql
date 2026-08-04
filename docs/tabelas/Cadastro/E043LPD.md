# E043LPD

## Descrição

Tabelas - Modelos de Planos - Ligação Plano Empresa X Município

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMpc | Number(004,0) | Não | Código do modelo de plano de contas |
| CodRai | Number(007,0) | Não | Código da cidade RAIS utilizada para apuração do ISS |
| CptIni | Date | Não | Data Competência Inicial |
| CtaRed | Number(009,0) | Não | Número reduzido da conta do modelo de plano |
| IdeCtd | Number(009,0) | Não | Código da tributação da Desif |
| CodEve | Number(003,0) | Não | Código do evento da Desif (Anexo 1) |

---

## Chave Primária

- CodMpc
- CodRai
- CptIni
- CtaRed

---

## Índices

### E008RAI_has_E043PCM_FKIndex1

**Tipo:** Não unico

Campos:
- CodRai

### E008RAI_has_E043PCM_FKIndex2

**Tipo:** Não unico

Campos:
- CodMpc
- CtaRed

### E008RAI_has_E043PCM_FKIndex3

**Tipo:** Não unico

Campos:
- IdeCtd

---

## Relacionamentos

### IR_E043LPD_003

**Tabela:** E043PCM

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |
| CtaRed | CtaRed |

