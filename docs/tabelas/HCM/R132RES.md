# R132RES

## Descrição

Reserva de curso - Agrupada por competência

---

## Resumo

- Campos: 21
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| CmpRea | Date | Não | Competência Realização |
| SeqTre | Number(002,0) | Não | Sequência da Reserva |
| OriRes | Number(001,0) | Sim | Origem da Reserva |
| CodFes | Number(008,0) | Sim | Código da Entidade |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| PerDia | String(001) | Sim | Período do Dia |
| PerIni | Date | Sim | Data Previsão de Início Treinamento |
| PerFim | Date | Sim | Data Previsão de Término Treinamento |
| CarHor | Number(010,0) | Sim | Carga Horária |
| VagRes | Number(006,0) | Sim | Vagas Reservadas |
| TipRea | Number(003,0) | Sim | Tipo de Realização |
| CodMcu | Number(003,0) | Sim | Motivo do Curso |
| ObsRet | String(200) | Sim | Observação |
| CodUsu | Number(010,0) | Sim | Código do Usuário que gerou a Reserva |
| TipCol | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Responsável pela Reserva |
| CodDia | Number(009,0) | Sim | Código Diagnóstico |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Código Local |

---

## Chave Primária

- NumEmp
- CodCua
- CmpRea
- SeqTre

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R132RES_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R132RES_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R132RES_013

**Tabela:** R128MCU

| Origem | Destino |
|--------|---------|
| CodMcu | CodMcu |

### IR_R132RES_020

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

