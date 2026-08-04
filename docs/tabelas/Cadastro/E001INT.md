# E001INT

## Descrição

Tabelas - Transações - Integrações

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodTns | String(005) | Não | Código da transação origem |
| TnsInt | String(005) | Não | Código da transação a ser chamada via integração |
| ModInt | String(003) | Não | Módulo pertencente a transação chamada via integração |
| FilInt | Number(005,0) | Sim | Código da filial para integração |

---

## Chave Primária

- CodEmp
- CodTns
- TnsInt

---

## Índices

### E001INTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- TnsInt

---

## Relacionamentos

### IR_E001INT_001

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTns | CodTns |

### IR_E001INT_002

**Tabela:** E001TNS

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| TnsInt | CodTns |

