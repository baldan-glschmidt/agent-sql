# E000EME

## Descrição

Tabelas - Integrações - Requisições Estoque

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
| NumEme | Number(009,0) | Não | Número do documento de entrada do movimento de estoque |
| SeqEme | Number(004,0) | Não | Sequência do produto ou serviço no documento |

---

## Chave Primária

- SeqInt

---

## Índices

### E000EMEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumEme
- SeqEme

---

## Relacionamentos

Nenhum relacionamento cadastrado.
