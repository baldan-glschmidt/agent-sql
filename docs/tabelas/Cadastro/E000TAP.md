# E000TAP

## Descrição

Tabelas - Integrações - Token Wiipo

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
| AppNam | String(100) | Não | Nome da aplicão |
| AppTkn | String(2000) | Sim | Informações do token |

---

## Chave Primária

- SeqInt

---

## Índices

### E000TAPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- AppNam
- AppTkn

---

## Relacionamentos

Nenhum relacionamento cadastrado.
