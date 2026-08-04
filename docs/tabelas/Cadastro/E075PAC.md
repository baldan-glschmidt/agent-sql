# E075PAC

## Descrição

Cadastros - Características - Ligação Produto X Agrupamento

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodAgp | String(005) | Não | Código do agrupamento |
| SeqRel | Number(009,0) | Não | Sequência do relacionamento |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| ObsPac | String(999) | Sim | Texto da observação da ligação |

---

## Chave Primária

- CodEmp
- CodAgp
- SeqRel
- CodPro
- CodDer

---

## Índices

### E075PACIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer

---

## Relacionamentos

### IR_E075PAC_001

**Tabela:** E010AGP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodAgp | CodAgp |

### IR_E075PAC_003

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E075PAC_004

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

