# R122CON

## Descrição

Candidatos Externos - Concurso

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| SitCan | Number(002,0) | Sim | Situação Candidato |
| NumIns | Number(008,0) | Sim | Número de inscrição do candidato |
| ObsCon | String(060) | Sim | Observações do Concurso |

---

## Chave Primária

- NumCan
- AnoCon
- NumCon
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CON_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CON_002

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R122CON_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

