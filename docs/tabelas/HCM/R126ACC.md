# R126ACC

## Descrição

Anúncios - Cargos do Concurso

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodVag | String(010) | Não | Código da Vaga usado na publicação do anúncio |
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código Cargo |

---

## Chave Primária

- CodVag
- AnoCon
- NumCon
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126ACC_000

**Tabela:** R126ANU

| Origem | Destino |
|--------|---------|
| CodVag | CodVag |

### IR_R126ACC_002

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R126ACC_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

