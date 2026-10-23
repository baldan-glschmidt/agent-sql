# R121DCA

## Descrição

Concurso - Documentos necessários por cargo

---

## Resumo

- Campos: 7
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
| TipDoc | Number(004,0) | Não | Tipo do Documento |
| IndObr | String(001) | Sim | Indicador de obrigatoriedade |
| ObsDoc | String(250) | Sim | Observação sobre documento |

---

## Chave Primária

- AnoCon
- NumCon
- EstCar
- CodCar
- TipDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121DCA_003

**Tabela:** R121CAR

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R121DCA_004

**Tabela:** R022DOC

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |

