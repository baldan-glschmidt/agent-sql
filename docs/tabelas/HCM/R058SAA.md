# R058SAA

## Descrição

Saídas dos Acionamentos

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| ModLei | Number(003,0) | Não | Modelo da Leitora |
| TipAci | Number(001,0) | Não | Tipo de Acionamento |
| CodSaa | Number(003,0) | Não | Código da Interface de Saída |
| DesSaa | String(030) | Sim | Descrição da Interface de Saída |
| TemSaa | Number(004,0) | Sim | Tempo Acionamento Saída (em escalas de 100 milissegundos) |

---

## Chave Primária

- ModRlg
- ModLei
- TipAci
- CodSaa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
