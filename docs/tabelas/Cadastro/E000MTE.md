# E000MTE

## Descrição

Tabelas - Integrações - Movimentos de Tesouraria

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumCco | String(014) | Não | Número da conta interna |
| DatMov | Date | Não | Data do movimento da conta |
| SeqMov | Number(006,0) | Não | Sequência na data do movimento da conta |
| IdeUni | String(050) | Sim | Identificador único alfanumérico |

---

## Chave Primária

- SeqInt

---

## Índices

### E000MTEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumCco
- DatMov
- SeqMov

---

## Relacionamentos

Nenhum relacionamento cadastrado.
