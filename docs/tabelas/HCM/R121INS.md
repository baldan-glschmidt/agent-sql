# R121INS

## Descrição

Concurso - Inscrição Candidato Interno

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| NumEmp | Number(004,0) | Não | Empresa do candidato |
| TipCol | Number(001,0) | Não | Tipo do candidato |
| NumCad | Number(009,0) | Não | Cadastro do candidato |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| SitCan | Number(001,0) | Sim | Situação Candidato |
| NumIns | Number(008,0) | Sim | Número de inscrição do candidato |
| ObsCon | String(700) | Sim | Observações do Concurso |

---

## Chave Primária

- AnoCon
- NumCon
- NumEmp
- TipCol
- NumCad
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121INS_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121INS_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

