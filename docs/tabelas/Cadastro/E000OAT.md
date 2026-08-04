# E000OAT

## Descrição

Tabelas - Integrações - Ocorrências Assistência Técnica

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
| FilOat | Number(005,0) | Não | Filial da ocorrência de assistência técnica |
| NumOat | Number(009,0) | Não | Número da Ocorrência (Protocolo) |

---

## Chave Primária

- SeqInt

---

## Índices

### E000OATIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- FilOat
- NumOat

---

## Relacionamentos

Nenhum relacionamento cadastrado.
