# E000EST

## Descrição

Tabelas - Integrações - Saldo de Estoque

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
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto em estoque |
| CodDer | String(007) | Não | Código da derivação do produto em estoque |
| CodDep | String(010) | Não | Código do depósito |

---

## Chave Primária

- SeqInt

---

## Índices

### E000ESTIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- CodDep

---

## Relacionamentos

Nenhum relacionamento cadastrado.
