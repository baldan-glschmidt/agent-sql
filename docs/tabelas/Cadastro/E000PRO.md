# E000PRO

## Descrição

Tabelas - Integrações - Produtos

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
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do Produto (tamanho, cor, etc.) |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PROIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
