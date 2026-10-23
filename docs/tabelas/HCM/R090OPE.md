# R090OPE

## Descrição

Pessoas Não Gratas Envolvidas nas Ocorrências da Portaria

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Site da Ocorrência |
| DatOcP | Date | Não | Data da Ocorrência na Portaria |
| HorOcP | Number(005,0) | Não | Hora da Ocorrência na Portaria |
| SeqOcP | Number(002,0) | Não | Sequência da Ocorrência na Portaria |
| SeqEnv | Number(002,0) | Não | Sequência da Pessoa Não Grata Envolvida na Ocorrência na Portaria |
| TipDoc | Number(001,0) | Não | Tipo do Documento da Pessoa Não Grata |
| NumDoc | String(020) | Não | Número do Documento da Pessoa Não Grata |

---

## Chave Primária

- CodPlt
- DatOcP
- HorOcP
- SeqOcP
- SeqEnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090OPE_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R090OPE_006

**Tabela:** R090PNG

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

