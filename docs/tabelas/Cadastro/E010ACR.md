# E010ACR

## Descrição

Cadastros - Características - Relacionamentos dos Agrupamentos

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodAgp | String(005) | Não | Código do agrupamento |
| SeqRel | Number(009,0) | Não | Sequência do relacionamento |
| CodCte | String(003) | Não | Código da característica de produto |
| SeqCcp | Number(009,0) | Não | Número da sequência da característica válido para o produto |

---

## Chave Primária

- CodEmp
- CodAgp
- SeqRel
- CodCte

---

## Índices

### E010ACRIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCte

### E010ACRIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodCte
- SeqCcp

---

## Relacionamentos

### IR_E010ACR_001

**Tabela:** E010AGP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodAgp | CodAgp |

### IR_E010ACR_003

**Tabela:** E010CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |

### IR_E010ACR_004

**Tabela:** E010CCP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |
| SeqCcp | SeqCcp |

