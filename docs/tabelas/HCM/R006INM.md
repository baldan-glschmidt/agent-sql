# R006INM

## Descrição

Intervalos - Marcações

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
| CodInt | Number(009,0) | Não | Código do Intervalo |
| SeqMar | Number(002,0) | Não | Sequência da Marcação |
| UsoBat | Number(002,0) | Sim | Uso da Marcação |
| HorBat | Number(005,0) | Sim | Hora da Marcação |
| TolAnt | Number(005,0) | Sim | Tolerância Antes da Marcação |
| TolApo | Number(005,0) | Sim | Tolerância Após a Marcação |
| FaiMov | Number(005,0) | Sim | Mobilidade da Marcação |

---

## Chave Primária

- CodInt
- SeqMar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R006INM_000

**Tabela:** R006INT

| Origem | Destino |
|--------|---------|
| CodInt | CodInt |

