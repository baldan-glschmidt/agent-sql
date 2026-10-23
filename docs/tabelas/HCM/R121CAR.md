# R121CAR

## Descrição

Concurso - Cargos

---

## Resumo

- Campos: 23
- Chave Primária: 4 campo(s)
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
| QtdVga | Number(004,0) | Sim | Quantidade de vaga do cargo/função |
| DesCon | String(420) | Sim | Descrição da condição para inscrição |
| DesPer | String(420) | Sim | Descrição do perfil desejado |
| DesReJ | String(420) | Sim | Descrição da regra de julgamento |
| DesReD | String(420) | Sim | Descrição da regra de desempate |
| RegCla | Number(003,0) | Sim | Regra para classificação dos candidatos |
| SitCon | String(001) | Sim | Identifica se o concurso está classificado |
| SitEta | String(001) | Sim | Identifica se as etapas estão avaliadas |
| TipRqu | Number(003,0) | Sim | Tipo Requisição |
| CodEsc | Number(009,0) | Sim | Código da escala |
| CodEst | Number(004,0) | Sim | Código da estrutura salarial |
| ClaSal | String(005) | Sim | Classe salarial |
| NivSal | String(005) | Sim | Nível salarial |
| TipSal | Number(001,0) | Sim | Tipo do salário |
| CodMot | Number(003,0) | Sim | Motivo do salário |
| ValSal | Number(013,4) | Sim | Valor do salário efetivo |
| ValIns | Number(013,4) | Sim | Valor da inscrição |
| VagPne | Number(004,0) | Sim | Quantidade de vagas para Pessoas com Deficiência |
| CarHor | Number(010,0) | Sim | Carga horária do concurso |

---

## Chave Primária

- AnoCon
- NumCon
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121CAR_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121CAR_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R121CAR_012

**Tabela:** R114RRQ

| Origem | Destino |
|--------|---------|
| TipRqu | CodRrq |

