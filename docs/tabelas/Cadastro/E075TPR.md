# E075TPR

## Descrição

Cadastros - Tabela de preço do produto produzido

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeOpr | Number(009,0) | Não | Identificador do registro de origem por produto/derivação |
| CodTpr | String(004) | Não | Código da tabela de preço |
| DatIni | Date | Não | Data de Inicio da Tabela de Preço |
| CodMod | String(014) | Não | Código do Modelo |
| CodFxa | String(015) | Não | Código da Faixa da Grade |

---

## Chave Primária

- IdeUni
- IdeOpr

---

## Índices

### E075TPRIndice1

**Tipo:** Não unico

Campos:
- IdeOpr

---

## Relacionamentos

### IR_E075TPR_001

**Tabela:** E075OPR

| Origem | Destino |
|--------|---------|
| IdeOpr | IdeUni |

