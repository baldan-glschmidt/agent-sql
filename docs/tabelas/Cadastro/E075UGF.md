# E075UGF

## Descrição

Tabelas - Integrações - Grupo Fiscal Produto x UF

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqUgf | Number(009,0) | Não | Número sequencial do registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| SigUfs | String(002) | Não | Sigla do estado |
| IdeNgf | Number(009,0) | Sim | Identificador do grupo fiscal |
| CodFil | Number(005,0) | Sim | Código da filial |

---

## Chave Primária

- SeqUgf

---

## Índices

### E075UGFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodPro
- CodDer
- SigUfs
- IdeNgf
- CodFil

### E075UGFIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

### E075UGFIndice3

**Tipo:** Não unico

Campos:
- IdeNgf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
