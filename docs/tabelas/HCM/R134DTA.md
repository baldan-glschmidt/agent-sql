# R134DTA

## Descrição

Turmas - Anônimos

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código Turma |
| SeqAno | Number(004,0) | Não | Sequência que individualiza o anônimo |
| ComPos | String(1600) | Sim | Comentário Positivo do Participante sobre o Curso |
| ComNeg | String(1600) | Sim | Comentário Negativo do Participante sobre o Curso |

---

## Chave Primária

- CodCua
- TmaCua
- SeqAno

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134DTA_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

