# E051MON

## Descrição

Cadastro de Alíquotas do CBS/IBS Monofásico

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodAnp | Number(009,0) | Não | Código ANP do produto |
| AliCBS | Number(007,4) | Não | Alíquota ad rem do CBS monofásico |
| AliIBS | Number(007,4) | Não | Alíquota ad rem do IBS monofásico |
| VigIni | Date | Não | Data de vigência inicial |
| DifCBS | Number(007,4) | Sim | Percentual de diferimento do CBS monofásico |
| DifIBS | Number(007,4) | Sim | Percentual de diferimento do IBS monofásico |
| UniMed | String(003) | Não | Unidade de medida da tributação |
| IndMis | Number(007,4) | Sim | Índice de mistura obrigatório |
| ObsMon | String(250) | Sim | Observação do cadastro monofásico |

---

## Chave Primária

- IdeUni

---

## Índices

### E051MONIndice1

**Tipo:** Unico

Campos:
- CodAnp
- VigIni

---

## Relacionamentos

### IR_E051MON_001

**Tabela:** E019ANP

| Origem | Destino |
|--------|---------|
| CodAnp | CodAnp |

### IR_E051MON_007

**Tabela:** E015MED

| Origem | Destino |
|--------|---------|
| UniMed | UniMed |

