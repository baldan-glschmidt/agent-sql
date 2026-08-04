# E000CES

## Descrição

Vendas/Compras - Controle de Entrada e Saída - Dados Gerais

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
| DatEnt | Date | Não | Data da entrada |
| SeqEnt | Number(006,0) | Não | Sequência de entrada  na data |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CESIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- DatEnt
- SeqEnt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
