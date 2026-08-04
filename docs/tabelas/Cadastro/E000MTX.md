# E000MTX

## Descrição

Pendências - Tesouraria - Fluxo de caixa SeniorX

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| NumCco | String(014) | Não | Número da Conta Interna |
| DatMov | Date | Não | Data do movimento da conta |
| SeqMov | Number(006,0) | Não | Sequência na data do movimento da conta |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| TipMov | String(001) | Não | Tipo de Movimento |

---

## Chave Primária

- CodEmp
- NumCco
- DatMov
- SeqMov

---

## Índices

### E000MTXIndice1

**Tipo:** Não unico

Campos:
- IdeUni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
