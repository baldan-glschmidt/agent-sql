# E000FER

## Descrição

Tabelas - Integrações - Feriados

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
| DiaFer | Number(002,0) | Não | Dia do Feriado |
| MesFer | Number(002,0) | Não | Mês do Feriado |
| AnoFer | Number(004,0) | Sim | Ano do feriado (caso ele ocorra uma única vez) |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade |

---

## Chave Primária

- SeqInt

---

## Índices

### E000FERIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- MesFer
- AnoFer
- CepIni
- DiaFer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
