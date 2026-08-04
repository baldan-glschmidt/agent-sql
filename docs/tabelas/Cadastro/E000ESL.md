# E000ESL

## Descrição

Tabelas - Integrações - Exportação Saldo de Lotes

---

## Resumo

- Campos: 9
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
| NumSep | String(050) | Não | Número de série do produto |
| CodLot | String(050) | Não | Código do lote de fabricação do produto |
| SeqEnt | Number(004,0) | Não | Sequência de entrada para o controle de lote |

---

## Chave Primária

- SeqInt

---

## Índices

### E000ESLIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- CodDep
- NumSep
- CodLot
- SeqEnt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
