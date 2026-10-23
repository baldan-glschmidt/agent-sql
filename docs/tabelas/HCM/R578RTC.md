# R578RTC

## Descrição

Avaliação de Competências - Resultado por Tipo de competência

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colaborador avaliado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador avaliado |
| NumCad | Number(009,0) | Não | Colaborador avaliado |
| CodCic | Number(003,0) | Não | Indica a qual Ciclo esta Avaliação pertence |
| IdeAva | Number(005,0) | Não | Identificador da avaliação de competências |
| CodTpC | Number(004,0) | Não | Tipo da Competência |
| NotRtc | Number(008,4) | Sim | Nota da avaliação para o Tipo da competência |
| PerRtc | Number(007,4) | Sim | Percentual de atingimento da avaliação para o Tipo da competência |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva
- CodTpC

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578RTC_004

**Tabela:** R578AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| IdeAva | IdeAva |

### IR_R578RTC_005

**Tabela:** R577TPC

| Origem | Destino |
|--------|---------|
| CodTpC | CodTpC |

