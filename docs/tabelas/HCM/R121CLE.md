# R121CLE

## Descrição

Concurso - Etapas da Solicitação

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| CodEta | Number(003,0) | Não | Código Etapa |
| TipAva | String(001) | Sim | Tipo de avaliação(N-Nota, P-Parecer) |
| PesEta | Number(002,0) | Sim | Peso da Etapa |
| NotApr | Number(006,2) | Sim | Nota mínima para aprovação(Nota de Corte) |
| AbrPar | String(050) | Sim | Abrangência de parecer aceitável para aprovação |
| IndEta | String(001) | Sim | Avaliação é do C-candidato ou P-processo |
| DatRea | Date | Sim | Data de realização para a etapa |
| HorIni | Number(005,0) | Sim | Hora início para realização da etapa |
| HorFim | Number(005,0) | Sim | Hora de término para realização da etapa |
| LocEta | String(100) | Sim | Local para realização da etapa |
| DatRes | Date | Sim | Data de resultado da etapa |
| SitEta | String(001) | Sim | Situação da etapa |
| RegAva | Number(003,0) | Sim | Regra para avaliação dos candidatos |
| DatVen | Date | Sim | Data de vencimento da etapa |

---

## Chave Primária

- AnoCon
- NumCon
- EstCar
- CodCar
- CodEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121CLE_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121CLE_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R121CLE_004

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

