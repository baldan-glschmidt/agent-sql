# E900EOO

## Descrição

O.P./O.S. - Movimentação OP/OS para o Painel OEE

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
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodEtg | Number(004,0) | Não | Código do estágio de produção |
| SeqEoq | Number(005,0) | Não | Sequência da movimentação da produção |

---

## Chave Primária

- IdeUni

---

## Índices

### E900EOOIndice2

**Tipo:** Unico

Campos:
- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqEoq

---

## Relacionamentos

Nenhum relacionamento cadastrado.
