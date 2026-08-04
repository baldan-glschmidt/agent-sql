# E095AIF

## Descrição

Cadastros - Fornecedores - Áreas de Interesse

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
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodAri | String(003) | Não | Código da área de interesse |
| ObsAif | String(030) | Sim | Observações da área de interesse do fornecedor |

---

## Chave Primária

- CodFor
- CodAri

---

## Índices

### E095AIFIndice1

**Tipo:** Não unico

Campos:
- CodAri

---

## Relacionamentos

### IR_E095AIF_000

**Tabela:** E095FOR

| Origem | Destino |
|--------|---------|
| CodFor | CodFor |

### IR_E095AIF_001

**Tabela:** E061ARI

| Origem | Destino |
|--------|---------|
| CodAri | CodAri |

