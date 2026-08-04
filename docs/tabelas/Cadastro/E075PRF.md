# E075PRF

## Descrição

Cadastros - Registros de familia de produto

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| FamAtu | String(006) | Não | Código da família atual do produto |
| FamNov | String(006) | Não | Código da família Nova do produto |
| IndAtu | String(001) | Não | indicativo se o produto foi atualizado |

---

## Chave Primária

- CodEmp
- CodPro

---

## Índices

### E075PRFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodPro
- FamAtu
- FamNov

---

## Relacionamentos

### IR_E075PRF_002

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| FamAtu | CodFam |

### IR_E075PRF_003

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| FamNov | CodFam |

