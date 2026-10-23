# R070CRI

## Descrição

Marcações Ponto Originais Criptografadas

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCra | String(060) | Não | Crachá Criptografado |
| DatAcc | Date | Não | Data da Marcação |
| HorAcc | Number(005,0) | Não | Hora da Marcação |
| SeqAcc | Number(002,0) | Não | Sequência da Marcação |
| DatApu | Date | Sim | Data da Apuração |
| StrMar | String(250) | Sim | Marcações Criptografadas |

---

## Chave Primária

- NumCra
- DatAcc
- HorAcc
- SeqAcc

---

## Índices

### R070CRIINDICE2

**Tipo:** Não unico

Campos:
- NumCra
- DatApu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
