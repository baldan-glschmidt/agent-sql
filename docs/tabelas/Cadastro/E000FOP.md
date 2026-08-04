# E000FOP

## Descrição

Tabelas - Integrações - Fotos de Produtos

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
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| SeqLpf | Number(004,0) | Não | Sequência de Fotos ligada ao Produto |

---

## Chave Primária

- SeqInt

---

## Índices

### E000FOPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- SeqLpf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
