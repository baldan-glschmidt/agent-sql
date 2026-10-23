# R210RES

## Descrição

Questionário - Respostas das perguntas

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodQue | Number(003,0) | Não | Código do Questionário |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| CodRes | Number(002,0) | Não | Código da Resposta |
| DesRes | String(1999) | Sim | Descrição da resposta |
| PesRes | Number(002,0) | Sim | Peso da resposta |
| ResCor | String(001) | Sim | Reposta Correta |
| ValMin | Number(011,2) | Sim | Valor mínimo para resposta |
| ValMax | Number(011,2) | Sim | Valor máximo para resposta |
| CodTbn | Number(003,0) | Sim | Código da Tabela de Notas da pergunta |

---

## Chave Primária

- CodQue
- CodPer
- CodRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R210RES_001

**Tabela:** R210PER

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |
| CodPer | CodPer |

