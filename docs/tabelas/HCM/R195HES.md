# R195HES

## Descrição

Cenário - Histórico Escalas

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração da Escala |
| CodEsc | Number(009,0) | Sim | Código da Nova Escala |
| CodTma | Number(001,0) | Sim | Código da Nova Turma da Escala |
| TurInt | Number(009,0) | Sim | Código da Turma de Intervalo |
| HorBas | Number(004,0) | Sim | Horário Base (Segunda a Sexta-Feira) |
| HorSab | Number(004,0) | Sim | Horário de Sábado |
| HorSem | Number(010,0) | Sim | Horas Semanais |
| HorDsr | Number(010,0) | Sim | Horas de DSR |
| GerCol | String(001) | Sim | Origem da geração do histórico |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195HES_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195HES_005

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

