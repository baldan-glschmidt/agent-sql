# E070CFO

## Descrição

Tabelas - Integrações - Tabela comparação operação integração - CFOP / Transação ERP

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro da ligação CFOP / transação ERP. |
| IdeOpn | Number(009,0) | Não | Identificador de registro da Operação |
| ComNat | String(005) | Sim | Natureza de operação (CFOP) |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação |

---

## Chave Primária

- IdeUni

---

## Índices

### E070CFOIndice1

**Tipo:** Unico

Campos:
- IdeOpn
- ComNat

---

## Relacionamentos

### IR_E070CFO_001

**Tabela:** E070OPN

| Origem | Destino |
|--------|---------|
| IdeOpn | IdeUni |

