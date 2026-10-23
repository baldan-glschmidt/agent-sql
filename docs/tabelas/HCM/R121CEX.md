# R121CEX

## Descrição

Concurso - Candidato Externo

---

## Resumo

- Campos: 23
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| SitCan | Number(002,0) | Sim | Situação Candidato |
| CodEta | Number(003,0) | Sim | Código da Etapa de eliminação |
| MotEli | Number(003,0) | Sim | Motivo da eliminação do candidato |
| MotDes | Number(003,0) | Sim | Motivo da desistência do candidato |
| NumCla | Number(006,0) | Sim | Ordem de classificação do candidato |
| DatDes | Date | Sim | Data de desistência do candidato |
| MedCan | Number(006,2) | Sim | Média do candidato |
| ClaSec | Number(006,0) | Sim | Ordem de classificação secundária do candidato |
| Val001 | Number(011,6) | Sim | Valor 1 para classificação |
| Val002 | Number(011,6) | Sim | Valor 2 para classificação |
| Val003 | Number(011,6) | Sim | Valor 3 para classificação |
| Val004 | Number(011,6) | Sim | Valor 4 para classificação |
| Val005 | Number(011,6) | Sim | Valor 5 para classificação |
| Val006 | Number(011,6) | Sim | Valor 6 para classificação |
| Val007 | Number(011,6) | Sim | Valor 7 para classificação |
| Val008 | Number(011,6) | Sim | Valor 8 para classificação |
| Val009 | Number(011,6) | Sim | Valor 9 para classificação |
| Val010 | Number(011,6) | Sim | Valor 10 para classificação |

---

## Chave Primária

- AnoCon
- NumCon
- NumCan
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121CEX_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121CEX_002

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R121CEX_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

