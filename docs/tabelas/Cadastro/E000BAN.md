# E000BAN

## Descrição

Tabelas - Integrações - Bancos

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
| CodBan | String(003) | Não | Código do banco na Febraban |

---

## Chave Primária

- SeqInt

---

## Índices

### E000BANIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodBan

---

## Relacionamentos

Nenhum relacionamento cadastrado.
