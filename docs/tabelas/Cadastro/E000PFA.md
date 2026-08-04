# E000PFA

## Descrição

Tabelas - Integrações - Clientes

---

## Resumo

- Campos: 5
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
| NumAne | Number(012,0) | Não | Número da análise de embarque |
| NumPfa | Number(009,0) | Não | Número da pré-fatura |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PFAIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumAne
- NumPfa

---

## Relacionamentos

### IR_E000PFA_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

