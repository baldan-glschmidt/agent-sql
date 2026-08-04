# E000MVI

## Descrição

Tabelas - Integração - Movimentos de Estoque - Controle de integração

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
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodInt | Number(002,0) | Não | Código da integração |
| IdeExt | Number(009,0) | Sim | Identificador externo do registro |
| CodPro | String(014) | Não | Código do produto movimentado |
| CodDer | String(007) | Não | Código da derivação do produto movimentado |
| CodDep | String(010) | Não | Código do depósito movimentado |
| DatMov | Date | Não | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |

---

## Chave Primária

- IdeUni

---

## Índices

### E000MVIIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodPro
- CodInt
- CodDer
- CodDep
- DatMov
- SeqMov

---

## Relacionamentos

Nenhum relacionamento cadastrado.
