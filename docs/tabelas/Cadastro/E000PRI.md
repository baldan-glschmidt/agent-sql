# E000PRI

## Descrição

Tabelas - Integrações - Prioridades de Compras

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
| CodPri | Number(009,0) | Não | Código da prioridade |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PRIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPri

---

## Relacionamentos

### IR_E000PRI_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

