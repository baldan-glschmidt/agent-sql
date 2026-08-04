# E000FPR

## Descrição

Tabelas - Integrações - Ligação Produto x Fornecedor

---

## Resumo

- Campos: 8
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
| CodFor | Number(009,0) | Não | Código do Fornecedor |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| SigUfs | String(002) | Não | Sigla do estado da filial |
| CodTns | String(005) | Não | Código da transação |

---

## Chave Primária

- SeqInt

---

## Índices

### E000FPRIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodFor
- CodPro
- CodDer
- SigUfs
- CodTns

---

## Relacionamentos

Nenhum relacionamento cadastrado.
