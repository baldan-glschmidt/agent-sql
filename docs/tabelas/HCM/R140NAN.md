# R140NAN

## Descrição

Notas do Curso - Anônimo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código Curso |
| TmaCua | Number(006,0) | Não | Código Turma |
| SeqAno | Number(004,0) | Não | Sequência que individualiza o anônimo |
| CodTnt | Number(003,0) | Não | Item de Nota do Curso |
| NotCur | Number(005,2) | Sim | Nota do Curso |
| ObsCur | String(500) | Sim | Observação sobre a nota do curso |

---

## Chave Primária

- CodCua
- TmaCua
- SeqAno
- CodTnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140NAN_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R140NAN_003

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

