# R134EHO

## Descrição

Turmas - Exceção Horário/Sala

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
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodHcu | Number(006,0) | Não | Código do Horário Curso |
| CodSla | Number(004,0) | Não | Código da Sala de Realização do Curso |
| DatExc | Date | Não | Data da Exceção |
| HorIni | Number(005,0) | Não | Hora Início da Exceção |
| HorTer | Number(005,0) | Sim | Hora Término da Exceção |
| ObsExc | String(200) | Sim | Observações da exceção de horário |

---

## Chave Primária

- CodCua
- TmaCua
- CodHcu
- CodSla
- DatExc
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134EHO_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134EHO_003

**Tabela:** R140SLA

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |

