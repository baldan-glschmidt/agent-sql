# E000SCO

## Descrição

Tabelas - Integrações - Saldo Contábil Mensal Centro Custo/Origem

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
| SeqInt | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| MesAno | Date | Não | Mês e ano de competência |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil |
| CodCcu | String(009) | Não | Código do centro de custos |
| OriLct | String(003) | Não | Origem do lançamento |

---

## Chave Primária

- SeqInt

---

## Índices

### E000SCOIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- MesAno
- CtaRed
- CodCcu
- OriLct

---

## Relacionamentos

Nenhum relacionamento cadastrado.
