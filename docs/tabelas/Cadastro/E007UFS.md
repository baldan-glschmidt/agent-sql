# E007UFS

## Descrição

Tabelas - Estados

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SigUfs | String(002) | Não | Sigla do estado |
| NomUfs | String(020) | Não | Nome do estado |
| CodPai | String(004) | Não | Código do país |
| AbrUfs | String(005) | Sim | Abreviatura do estado |

---

## Chave Primária

- SigUfs

---

## Índices

### E007UFSIndice1

**Tipo:** Não unico

Campos:
- CodPai

---

## Relacionamentos

### IR_E007UFS_002

**Tabela:** E006PAI

| Origem | Destino |
|--------|---------|
| CodPai | CodPai |

