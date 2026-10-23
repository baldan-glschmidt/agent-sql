# R210PER

## Descrição

Questionário - Perguntas

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodQue | Number(003,0) | Não | Código do Questionário |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| DesPer | String(3999) | Sim | Descrição da pergunta |
| CodAss | Number(003,0) | Sim | Código do assunto da pergunta |
| SeqPer | Number(003,0) | Sim | Sequência em que a pergunta deverá aparecer no questionário |
| TipPeQ | String(001) | Sim | Define qual é o Tipo da Pergunta |
| TemObs | String(001) | Sim | Define se a pergunta possui uma Observação |
| DesObs | String(060) | Sim | Define a descrição da Observação |
| ValMin | Number(011,2) | Sim | Valor mínimo para resposta |
| ValMax | Number(011,2) | Sim | Valor máximo para resposta |
| CodTbn | Number(003,0) | Sim | Código da Tabela de Notas da pergunta |

---

## Chave Primária

- CodQue
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R210PER_000

**Tabela:** R210QUE

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |

