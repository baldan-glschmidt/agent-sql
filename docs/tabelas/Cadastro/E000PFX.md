# E000PFX

## Descrição

Gerais - Integração de pré-faturas com seniorX

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqItx | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumAne | Number(012,0) | Não | Número da análise de embarque |
| NumPfa | Number(009,0) | Não | Número da pré-fatura |
| IdeUni | String(050) | Sim | Identificador único da pré-fatura na integração com seniorX |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- SeqItx

---

## Índices

### E000PFXIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumAne
- NumPfa

---

## Relacionamentos

Nenhum relacionamento cadastrado.
