# R182ITR

## Descrição

PLR - Itens de Questionário - Respostas

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodIte | Number(003,0) | Não | Código do Item |
| RspPpr | Number(011,2) | Não | Resposta (Nota) |
| DspPpr | String(030) | Sim | Descrição da Resposta |

---

## Chave Primária

- CodIte
- RspPpr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R182ITR_000

**Tabela:** R182ITE

| Origem | Destino |
|--------|---------|
| CodIte | CodIte |

