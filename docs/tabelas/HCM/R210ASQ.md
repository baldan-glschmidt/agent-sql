# R210ASQ

## Descrição

Questionário - Assuntos

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodQue | Number(003,0) | Não | Código do Questionário |
| CodAss | Number(003,0) | Não | Código do Assunto |
| OrdAss | Number(003,0) | Sim | Define em qual ordem o assunto será apresentado |
| CalAss | String(001) | Sim | Define como o deve ser o cálculo do Assunto |

---

## Chave Primária

- CodQue
- CodAss

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R210ASQ_000

**Tabela:** R210QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

### IR_R210ASQ_001

**Tabela:** R210ASS

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |

