# E000PLA

## Descrição

Tabelas - Integrações - Plano de Conta Contábil

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
| SeqInt | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CtaRed | Number(007,0) | Não | Conta contábil reduzida |
| GruCta | Number(001,0) | Não | Grupo que a conta contábil pertence |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PLAIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CtaRed

---

## Relacionamentos

Nenhum relacionamento cadastrado.
