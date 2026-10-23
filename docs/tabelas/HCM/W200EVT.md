# W200EVT

## Descrição

Tabela para histórico de execução dos processos

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo de workflow |
| ELEMID | Number(005,0) | Não | Identificador do elemento que gerou a pendência dona desta delegação |
| PRCSTP | Number(008,0) | Não | Passo do processo onde a atividade foi executada |
| EVTDAT | Date | Sim | Data em que o evento aconteceu |
| EVTTIM | Number(005,0) | Sim | Tempo em que aconteceu o evento |
| EVTSEQ | Number(005,0) | Não | Sequencial para o evento do histórico |
| EVTTYP | Number(005,0) | Sim | Tipo do evento de histórico |
| EVTVAL | String(2000) | Sim | Valor do histórico |

---

## Chave Primária

- PRCIID
- ELEMID
- PRCSTP
- EVTSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
