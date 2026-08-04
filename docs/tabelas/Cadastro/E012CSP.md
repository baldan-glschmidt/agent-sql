# E012CSP

## Descrição

Cadastros - Famílias - Características

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
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFam | String(006) | Não | Código da família de produtos |
| CodCte | String(003) | Não | Código da característica de produto vinculada à família |
| SitCsp | String(001) | Não | Situação |

---

## Chave Primária

- CodEmp
- CodFam
- CodCte

---

## Índices

### E012CSPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCte

---

## Relacionamentos

### IR_E012CSP_001

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E012CSP_002

**Tabela:** E010CTE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCte | CodCte |

