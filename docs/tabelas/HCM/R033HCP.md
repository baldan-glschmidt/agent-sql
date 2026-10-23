# R033HCP

## Descrição

Histórico de Competências da Pessoa

---

## Resumo

- Campos: 22
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SeqHis | Number(008,0) | Não | Informe um número sequencial para identificar o histórico |
| DatHis | Date | Sim | Determina a data em que a competência foi adquirida pela pessoa |
| CodCpt | Number(009,0) | Sim | Determina a Competência adquirida na data informada |
| RevCpt | String(010) | Sim | Determina qual Revisão da Competência foi adquirida na data informada |
| PrfApl | Number(004,0) | Sim | Indica qual foi o Perfil de aplicação adquirido para esta competência |
| CodTpr | Number(004,0) | Sim | Tabela de proficiências da revisão da competência adquirida |
| CodCPr | String(010) | Sim | Determina qual Conceito foi adquirido para a competência |
| NotCpt | Number(008,4) | Sim | Determina a nota adquirida para a Competência |
| DatVal | Date | Sim | Validade da Competência adquirida, ou seja, quando a aquisição vence |
| IndCer | String(001) | Sim | Indica se a aquisição desta Competência foi certificada |
| PerCpt | Number(007,4) | Sim | Indica o quanto (%) foi adquirido em relação a nota máxima |
| ObsHis | String(4000) | Sim | Observações sobre a aquisição da competência |
| OriHis | Number(001,0) | Sim | Indica a origem da aquisição da Competência |
| CodUsu | Number(009,0) | Sim | Usuário responsável pelo último registro no histórico |
| DthMod | Number(014,6) | Sim | Data/Hora da última modificação no registro do histórico |
| CodCic | Number(003,0) | Sim | Ciclo de avaliação que deu origem ao histórico |
| NumEmp | Number(004,0) | Sim | Empresa do colaborador |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Colaborador que deu origem ao histórico da competência |
| OriReg | Number(001,0) | Sim | Origem do registro do histórico de competência |
| SeqOri | Number(008,0) | Sim | Sequência de origem do registro (conforme origem do registro) |

---

## Chave Primária

- CodPes
- SeqHis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033HCP_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

### IR_R033HCP_004

**Tabela:** R577REV

| Origem | Destino |
|--------|---------|
| CodCpt | CodCpt |
| RevCpt | RevCpt |

### IR_R033HCP_007

**Tabela:** R577CPR

| Origem | Destino |
|--------|---------|
| CodTpr | CodTpr |
| CodCPr | CodCPr |

