# R121FCM

## Descrição

Concurso - Fórmula de Cálculo da Média

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |
| SeqFCM | Number(003,0) | Não | Sequência da fórmula de cálculo da média |
| OriVl1 | Number(001,0) | Sim | Origem do primeiro valor |
| Val001 | Number(010,6) | Sim | Valor 1 |
| CodEt1 | Number(003,0) | Sim | Código da Etapa de origem do Valor 1 |
| Seq001 | Number(003,0) | Sim | Sequência de origem do Valor 1 |
| OriVl2 | Number(001,0) | Sim | Origem do segundo valor |
| Val002 | Number(010,6) | Sim | Valor 2 |
| CodEt2 | Number(003,0) | Sim | Código da Etapa de origem do Valor 2 |
| Seq002 | Number(003,0) | Sim | Sequência de origem do Valor 2 |
| OpeFCM | Number(001,0) | Sim | Operação entre Valor 1 e Valor 2 |

---

## Chave Primária

- AnoCon
- NumCon
- EstCar
- CodCar
- SeqFCM

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121FCM_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121FCM_003

**Tabela:** R121CAR

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |
| EstCar | EstCar |
| CodCar | CodCar |

