# E000CNV

## Descrição

Tabelas - Integrações - Convênios

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
| CodCnv | Number(004,0) | Não | Código do convênio |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CNVIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCnv

---

## Relacionamentos

### IR_E000CNV_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

