# R121CEE

## Descrição

Concurso - Etapas Realizadas Candidato Externo

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| CodEta | Number(003,0) | Não | Código da Etapa |
| DatRea | Date | Sim | Data de realização da etapa |
| NotCan | Number(006,2) | Sim | Nota do candidato |
| CodPar | Number(003,0) | Sim | Código do parecer |

---

## Chave Primária

- AnoCon
- NumCon
- NumCan
- CodEta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121CEE_001

**Tabela:** R121CON

| Origem | Destino |
|--------|---------|
| AnoCon | AnoCon |
| NumCon | NumCon |

### IR_R121CEE_002

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R121CEE_003

**Tabela:** R114ETA

| Origem | Destino |
|--------|---------|
| CodEta | CodEta |

