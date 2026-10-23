# R121OCL

## Descrição

Concurso - Ordem de classificação

---

## Resumo

- Campos: 8
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
| SeqOcl | Number(002,0) | Não | Sequência de classificação |
| TipOcl | Number(001,0) | Sim | Tipo de Ordem de Classificação |
| AscDes | Number(001,0) | Sim | Ordem Ascendente/Descendente |
| CodEta | Number(003,0) | Sim | Código Etapa |

---

## Chave Primária

- AnoCon
- NumCon
- EstCar
- CodCar
- SeqOcl

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121OCL_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121OCL_003

**Tabela:** R121CAR

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |
| EstCar | EstCar |
| CodCar | CodCar |

