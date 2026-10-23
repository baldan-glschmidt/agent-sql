# R004MHR

## Descrição

Marcações do Horário

---

## Resumo

- Campos: 7
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHor | Number(004,0) | Não | Código do Horário |
| SeqMar | Number(002,0) | Não | Sequência da Marcação |
| UsoBat | Number(002,0) | Sim | Uso da Marcação |
| HorBat | Number(005,0) | Sim | Hora da Marcação |
| TolAnt | Number(005,0) | Sim | Tolerância Antes |
| TolApo | Number(005,0) | Sim | Tolerância Após |
| FaiMov | Number(005,0) | Sim | Mobilidade da Marcação |

---

## Chave Primária

- CodHor
- SeqMar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R004MHR_000

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

