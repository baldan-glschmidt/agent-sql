# E000DEP

## Descrição

Tabelas - Integrações - Depósitos

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodDep | String(010) | Não | Código do depósito |

---

## Chave Primária

- SeqInt

---

## Índices

### E000DEPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodDep

---

## Relacionamentos

### IR_E000DEP_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

