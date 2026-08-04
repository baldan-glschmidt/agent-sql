# E000SOL

## Descrição

Tabelas - Integrações - Solicitação de Compra

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
| NumSol | Number(009,0) | Não | Número do documento da solicitação |
| SeqSol | Number(006,0) | Não | Sequência do item na solicitação de compras |

---

## Chave Primária

- SeqInt

---

## Índices

### E000SOCIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumSol
- SeqSol

---

## Relacionamentos

Nenhum relacionamento cadastrado.
