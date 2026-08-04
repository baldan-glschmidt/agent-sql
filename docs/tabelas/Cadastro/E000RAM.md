# E000RAM

## Descrição

Tabelas - Integrações - Ramos de atividade

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
| CodRam | String(005) | Não | Código do ramo de atividade |

---

## Chave Primária

- SeqInt

---

## Índices

### E000RAMIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodRam

---

## Relacionamentos

Nenhum relacionamento cadastrado.
