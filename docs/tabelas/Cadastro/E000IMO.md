# E000IMO

## Descrição

Tabelas - Integrações - Índices Moedas

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
| CodMoe | String(003) | Não | Código da moeda ou índice |
| DatMoe | Date | Não | Data da cotação da moeda ou índice |

---

## Chave Primária

- SeqInt

---

## Índices

### E000IMOIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodMoe
- DatMoe

---

## Relacionamentos

Nenhum relacionamento cadastrado.
