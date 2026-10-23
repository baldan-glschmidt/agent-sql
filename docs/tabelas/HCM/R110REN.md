# R110REN

## Descrição

Medicamentos - Entradas em estoque

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRem | Number(006,0) | Não | Código do Medicamento |
| CodPos | Number(007,0) | Não | Código do posto  de atendimento |
| DatEnt | Date | Não | Data de entrada de medicamento em estoque |
| SeqEnt | Number(002,0) | Não | Sequência da entrada de medicamento em estoque |
| QtdEnt | Number(010,4) | Sim | Quantidade de medicamento |
| CodJus | Number(003,0) | Sim | Código da justificativa |
| FusHor | Number(002,0) | Sim | Fuso Horário |

---

## Chave Primária

- CodRem
- CodPos
- DatEnt
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110REN_000

**Tabela:** R110REM

| Origem | Destino |
|--------|---------|
| CodRem | CodRem |

