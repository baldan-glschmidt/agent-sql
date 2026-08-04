# E081TES

## Descrição

Tabelas - Tabela de Preço de Venda - ICMS por Estado

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTpr | String(004) | Não | Código da tabela de preço |
| SigUfs | String(002) | Não | Sigla do estado |
| IcmSco | Number(004,2) | Sim | Percentual de ICMS de saída para contribuintes |

---

## Chave Primária

- CodEmp
- CodTpr
- SigUfs

---

## Índices

### E081TESIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E081TES_001

**Tabela:** E081TAB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTpr | CodTpr |

### IR_E081TES_002

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

