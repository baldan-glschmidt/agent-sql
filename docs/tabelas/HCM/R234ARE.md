# R234ARE

## Descrição

Evento - Avaliação de Reação

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
| CodEvn | Number(009,0) | Não | Código do Evento |
| SeqARe | Number(004,0) | Não | Sequência da avaliação de reação |
| IdePar | String(024) | Sim | Identificação do Participante na Avaliação de Reação |
| CodPes | Number(009,0) | Sim | Código da Pessoa |
| AReCon | String(001) | Sim | Avaliação de Reação Concluída |
| ComPos | String(1600) | Sim | Comentário Positivo do Participante sobre o Evento |
| ComNeg | String(1600) | Sim | Comentário Negativo do Participante sobre o Evento |

---

## Chave Primária

- CodEvn
- SeqARe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R234ARE_000

**Tabela:** R234EVN

| Origem | Destino |
|--------|---------|
| CodEvn | CodEvn |

