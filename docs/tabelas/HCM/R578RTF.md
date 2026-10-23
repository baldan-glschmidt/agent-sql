# R578RTF

## Descrição

Avaliação de Competências - Avaliação por foco - Resultado por Tipo de competência

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
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
| SeqAvf | Number(007,0) | Não | Sequência da avaliação por foco, dentro da avaliação do colaborador |
| CodTpC | Number(004,0) | Não | Tipo da Competência |
| NotRtf | Number(008,4) | Sim | Nota da avaliação para o Tipo da competência |
| PerRtf | Number(007,4) | Sim | Percentual de atingimento da avaliação para o Tipo da competência |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva
- SeqAvf
- CodTpC

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578RTF_005

**Tabela:** R578AVF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| IdeAva | IdeAva |
| SeqAvf | SeqAvf |

### IR_R578RTF_006

**Tabela:** R577TPC

| Origem | Destino |
|--------|---------|
| CodTpC | CodTpC |

