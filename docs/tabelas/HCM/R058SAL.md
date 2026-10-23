# R058SAL

## Descrição

Saídas dos Acionamentos de Alarmes

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
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| EntRel | Number(001,0) | Não | Entrada Digital Relacionada |
| CodSal | Number(003,0) | Não | Código da Interface de Saída do Alarme |
| TemSal | Number(004,0) | Sim | Tempo do Acionamento da Saída do Alarme (em escalas de 100 milissegundos) |
| DepAlm | String(001) | Sim | Dependente de Alarme |

---

## Chave Primária

- ModRlg
- EntRel
- CodSal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
