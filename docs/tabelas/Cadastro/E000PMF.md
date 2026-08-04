# E000PMF

## Descrição

Tabelas - Integrações - Preço Médio de Produto

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |

---

## Chave Primária

- SeqInt

---

## Índices

### E000PMFIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

### E000PMFIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
