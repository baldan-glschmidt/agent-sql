# R132RPA

## Descrição

Reserva de Curso - Por Participante

---

## Resumo

- Campos: 25
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do curso de aperfeiçoamento |
| NumEmp | Number(004,0) | Não | Código da empresa do participante da reserva |
| TipCol | Number(001,0) | Não | Tipo do colaborador participante da reserva |
| NumCad | Number(009,0) | Não | Cadastro do colaborador participante da reserva |
| DatRes | Date | Não | Data de cadastro da reserva |
| OriRes | Number(001,0) | Sim | Origem da reserva |
| CodMcu | Number(003,0) | Sim | Motivo da reserva de curso |
| CodUsu | Number(010,0) | Sim | Código do usuário que gerou a reserva |
| EmpRes | Number(004,0) | Sim | Código da empresa do responsável pela reserva |
| TipRes | Number(001,0) | Sim | Tipo do colaborador responsável pela reserva |
| CadRes | Number(009,0) | Sim | Cadastro do colaborador responsável pela reserva |
| PerIni | Date | Sim | Data previsão de início treinamento |
| PerFim | Date | Sim | Data previsão de término treinamento |
| ObsRes | String(250) | Sim | Observação |
| PerDia | String(001) | Sim | Período do dia |
| CodOem | Number(008,0) | Sim | Código da entidade de ensino |
| CodCid | Number(007,0) | Sim | Código da cidade |
| CarHor | Number(010,0) | Sim | Carga Horária |
| TipRea | Number(003,0) | Sim | Tipo de realização |
| TmaCua | Number(006,0) | Sim | Código  da turma |
| SolAux | String(001) | Sim | Define se deseja solicitar auxílio ao gravar reserva individual |
| CodCla | Number(003,0) | Sim | Definição da classificação das turmas |
| CodEvn | Number(009,0) | Sim | Código do Evento |
| USU_Ativid | String(300) | Sim | Atividade |
| USU_ResEsp | String(300) | Sim | Resultados Esperados |

---

## Chave Primária

- CodCua
- NumEmp
- TipCol
- NumCad
- DatRes

---

## Índices

### R132RPAIndice2

**Tipo:** Não unico

Campos:
- CodCua
- NumEmp
- TipCol
- NumCad
- TmaCua

---

## Relacionamentos

### IR_R132RPA_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132RPA_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R132RPA_006

**Tabela:** R128MCU

| Origem | Destino |
|--------|---------|
| CodMcu | CodMcu |

