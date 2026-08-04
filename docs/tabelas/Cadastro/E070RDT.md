# E070RDT

## Descrição

Cadastros - Filiais - Restrições de Destinatários em Notas Fiscais de Transferência

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
| SeqRdt | Number(009,0) | Não | Sequência da Restrição de Destinatários em Notas Fiscais de Transferência |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodCli | Number(009,0) | Não | Código do Cliente Restrito |
| SitRdt | String(001) | Não | Situação do registro |

---

## Chave Primária

- SeqRdt

---

## Índices

### E070RDT_UNIQUE

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCli

---

## Relacionamentos

Nenhum relacionamento cadastrado.
