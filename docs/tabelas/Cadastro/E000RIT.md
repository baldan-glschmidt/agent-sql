# E000RIT

## Descrição

Tabelas - Integrações - Retorno de chaves integradas do ERP

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
| SeqRip | Number(009,0) | Sim | Número sequencial dos registros de retorno da integração |

---

## Chave Primária

- SeqInt

---

## Índices

### E000RITIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- SeqRip

---

## Relacionamentos

Nenhum relacionamento cadastrado.
