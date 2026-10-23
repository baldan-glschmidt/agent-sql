# R038HES

## Descrição

Histórico Escalas

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
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
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| CodEqp | Number(004,0) | Sim | Código da Equipe |
| CodCat | Number(003,0) | Sim | Código da Categoria |
| DesSim | String(999) | Sim | Descrição da jornada para o eSocial Simplificado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HESIndice2

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

### R038HESIndice3

**Tipo:** Não unico

Campos:
- CodEsc

---

## Relacionamentos

### IR_R038HES_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HES_004

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

