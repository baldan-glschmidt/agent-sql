# R126ITQ

## Descrição

Requisições - Itens Questionário

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código da Requisição |
| CodItq | Number(003,0) | Não | Código do Item Questionário |
| AbrRes | String(050) | Sim | Abrangência Resposta Item Questionário |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| SeqItq | Number(003,0) | Sim | Sequência da pergunta |
| PtsItq | Number(002,0) | Sim | Pontuação do Item de Questionário |

---

## Chave Primária

- CodRqu
- CodItq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126ITQ_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R126ITQ_001

**Tabela:** R118ITQ

| Origem | Destino |
|--------|---------|
| CodItq | CodItq |

