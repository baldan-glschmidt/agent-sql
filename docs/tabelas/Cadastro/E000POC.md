# E000POC

## Descrição

Tabelas - Integrações - Ordem de Compra

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
| NumOcp | Number(008,0) | Não | Número da ordem de compra |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000POCIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumOcp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
