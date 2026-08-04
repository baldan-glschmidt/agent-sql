# E000POR

## Descrição

Tabelas - Integrações - Portadores

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
| CodPor | String(004) | Não | Código interno do portador (carteira, representante, advogado, bancos, etc..) |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PORIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPor

---

## Relacionamentos

Nenhum relacionamento cadastrado.
