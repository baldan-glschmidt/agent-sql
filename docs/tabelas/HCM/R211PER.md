# R211PER

## Descrição

Pesquisa - Definição - Perguntas respondidas

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
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
| ResSub | String(2999) | Sim | Resposta subjetiva (Questão subjetiva) |
| ValRes | Number(011,2) | Sim | Valor respondido (Questão quantitativa) |
| ValPes | Number(011,2) | Sim | Valor respondido com peso aplicado (Questão quantitativa) |
| DatRes | Date | Sim | Data respondida (Questão do tipo data) |
| ObsRes | String(2499) | Sim | Observação respondida (Questões com observação) |

---

## Chave Primária

- CodPsq
- SeqPsq
- SeqIde
- CodQue
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211PER_002

**Tabela:** R211IDP

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |
| SeqPsq | SeqPsq |
| SeqIde | SeqIde |

### IR_R211PER_004

**Tabela:** R210PER

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |
| CodPer | CodPer |

