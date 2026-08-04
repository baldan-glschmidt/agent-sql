# E440CNF

## Descrição

Compras - Contagens de Produtos - Notas Conferência

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumCnt | Number(009,0) | Não | Número da contagem |
| SeqCnt | Number(009,0) | Não | Sequência da nota conferida na contagem |
| EmpNfc | Number(004,0) | Sim | Código da empresa da nota fiscal de entrada |
| FilNfc | Number(005,0) | Sim | Código da filial da nota fiscal de entrada |
| ForNfc | Number(009,0) | Sim | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| SnfNfc | String(003) | Sim | Código da série da nota fiscal de entrada |

---

## Chave Primária

- CodEmp
- CodFil
- NumCnt
- SeqCnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
