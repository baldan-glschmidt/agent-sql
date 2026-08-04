# E070RET

## Descrição

Cadastros - Filiais - Ligação Filial X Locais de Retirada

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa. |
| CodFil | Number(005,0) | Não | Código da filial. |
| CodRet | Number(004,0) | Não | Código do local de retirada. |

---

## Chave Primária

- CodEmp
- CodFil
- CodRet

---

## Índices

### E070RETIndice1

**Tipo:** Não unico

Campos:
- CodRet

---

## Relacionamentos

### IR_E070RET_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E070RET_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E070RET_002

**Tabela:** E062RET

| Origem | Destino |
|--------|---------|
| CodRet | CodRet |

