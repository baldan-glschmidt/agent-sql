# R122EEL

## Descrição

Candidatos Externos - Endereços eletrônicos

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| CodEEl | Number(004,0) | Não | Código do tipo de endereço eletrônico |
| SeqEEl | Number(002,0) | Não | Sequência |
| EndEle | String(250) | Sim | Endereço eletrônico |

---

## Chave Primária

- NumCan
- CodEEl
- SeqEEl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122EEL_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122EEL_001

**Tabela:** R022EEL

| Origem | Destino |
|--------|---------|
| CodEEl | CodEEl |

