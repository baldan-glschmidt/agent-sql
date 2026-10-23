# R960PAR

## Descrição

Parâmetros de processamentos de multicamada

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IDREQ | String(020) | Não | Identificador da requisição |
| TIPPAR | Number(003,0) | Não | tipo dos parâmetros (0=Input; 1=Output) |
| IDSEQ | Number(003,0) | Não | Seqüência |
| PARVAL | Image | Sim | Valores dos parâmetros do processamento |

---

## Chave Primária

- IDREQ
- TIPPAR
- IDSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R960PAR_000

**Tabela:** R960REQ

| Origem | Destino |
|--------|---------|
| IDREQ | IDREQ |

