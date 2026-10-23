# R211RES

## Descrição

Pesquisa - Definição - Respostas respondidas

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPsq | Number(006,0) | Não | Código da Pesquisa |
| SeqPsq | Number(002,0) | Não | Sequência da pesquisa |
| SeqIde | Number(005,0) | Não | Sequência da identificação |
| CodQue | Number(003,0) | Não | Código do Questionário respondido |
| CodPer | Number(003,0) | Não | Código da Pergunta respondida |
| CodRes | Number(002,0) | Não | Código da Resposta respondida |
| ResAss | String(001) | Sim | Identifica se a resposta foi assinalada |
| ValRes | Number(011,2) | Sim | Valor respondido (Questão do tipo prioridade) |
| ValPes | Number(011,2) | Sim | Valor respondido com peso aplicado |

---

## Chave Primária

- CodPsq
- SeqPsq
- SeqIde
- CodQue
- CodPer
- CodRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211RES_002

**Tabela:** R211IDP

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |
| SeqPsq | SeqPsq |
| SeqIde | SeqIde |

### IR_R211RES_005

**Tabela:** R210RES

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |
| CodPer | CodPer |
| CodRes | CodRes |

