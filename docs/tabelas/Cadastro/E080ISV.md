# E080ISV

## Descrição

Tabelas - Serviços - Parametrizações de Intermediação

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumSeq | Number(009,0) | Não | Número sequencial do registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| SerInt | String(001) | Sim | Indica o tipo de serviço para ser ou não intermediado |
| IndIsv | String(001) | Sim | Indicativo se o tipo de serviço é vendido através de intermediação |
| TnsIsv | String(005) | Sim | Transação de intermediação de serviços |
| TnsDev | String(005) | Sim | Transação de devolução de intermediação de serviços |

---

## Chave Primária

- NumSeq

---

## Índices

### E080ISVIndice1

**Tipo:** Unico

Campos:
- SerInt
- CodEmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
