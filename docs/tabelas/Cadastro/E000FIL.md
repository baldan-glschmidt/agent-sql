# E000FIL

## Descrição

Tabelas - Integrações - Filiais

---

## Resumo

- Campos: 3
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

---

## Chave Primária

- SeqInt

---

## Índices

### E000FILIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E000FIL_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

