# E010ACI

## Descrição

Cadastros - Características - Itens dos Agrupamentos

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
| CodAgp | String(005) | Não | Código do agrupamento |
| CodCte | String(003) | Não | Código da característica de produto |
| SeqCte | Number(002,0) | Sim | Sequência da característica no agrupamento |

---

## Chave Primária

- CodEmp
- CodAgp
- CodCte

---

## Índices

### E010ACIIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCte

---

## Relacionamentos

### IR_E010ACI_001

**Tabela:** E010AGP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodAgp | CodAgp |

### IR_E010ACI_002

**Tabela:** E010CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |

