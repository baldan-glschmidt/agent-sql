# R077RCA

## Descrição

Hab. Técnicas - Req. Cursos Aperfeiçoamento

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| PesCua | Number(002,0) | Sim | Peso do Curso |

---

## Chave Primária

- CodHte
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077RCA_000

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

### IR_R077RCA_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

