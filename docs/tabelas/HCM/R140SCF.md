# R140SCF

## Descrição

Ocupação Extraordinária - Horário Coffee Break

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSla | Number(004,0) | Não | Código da Sala de Treinamento |
| DatOcu | Date | Não | Data Ocupação da Sala |
| HorIni | Number(005,0) | Não | Hora Início da Ocupação |
| SeqCbk | Number(002,0) | Não | Sequência do Registro |
| HorCbk | Number(005,0) | Sim | Horário do Início do Coffee Break |
| CodCbk | Number(003,0) | Sim | Código do Tipo de Coffee Break |
| DesCbk | String(030) | Sim | Descrição do Coffee Break |
| DesPro | String(500) | Sim | Providências |

---

## Chave Primária

- CodSla
- DatOcu
- HorIni
- SeqCbk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140SCF_000

**Tabela:** R140SLA

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |

### IR_R140SCF_002

**Tabela:** R140SOC

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |
| DatOcu | DatOcu |
| HorIni | HorIni |

