# E000PME

## Descrição

Tabelas - Integrações - Preço Médio Movimentos de Estoque

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodDep | String(010) | Não | Código do depósito |
| DatMov | Date | Não | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |
| NumEme | Number(009,0) | Não | Número do documento de entrada do movimento de estoque |
| SeqEme | Number(004,0) | Não | Sequência do produto ou serviço no documento |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PMEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- CodDep
- DatMov
- SeqMov
- NumEme
- SeqEme

---

## Relacionamentos

Nenhum relacionamento cadastrado.
