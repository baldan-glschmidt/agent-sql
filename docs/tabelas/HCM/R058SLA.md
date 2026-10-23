# R058SLA

## Descrição

Saídas dos Acionamentos de Leitoras

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| TipAci | Number(001,0) | Não | Tipo de Acionamento |
| CodSai | Number(009,0) | Não | Código do Dispositivo de Saída |
| DesSaa | String(030) | Sim | Descrição da Interface de Saída |
| TemSaa | Number(004,0) | Sim | Tempo Acionamento Saída (em escalas de 100 milissegundos) |

---

## Chave Primária

- CodDsp
- TipAci
- CodSai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
