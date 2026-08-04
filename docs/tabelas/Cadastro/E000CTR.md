# E000CTR

## Descrição

Tabelas - Integrações - Contrato de Venda

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumCtr | Number(009,0) | Não | Número interno do contrato |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CTRIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumCtr

---

## Relacionamentos

Nenhum relacionamento cadastrado.
