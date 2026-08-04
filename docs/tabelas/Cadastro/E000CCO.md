# E000CCO

## Descrição

Tabelas - Integrações - Contas Internas

---

## Resumo

- Campos: 4
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
| NumCco | String(014) | Não | Número da Conta Interna |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CCOIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumCco

---

## Relacionamentos

Nenhum relacionamento cadastrado.
