# R077RCF

## Descrição

Hab. Técnicas - Req. Cursos Formação

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| SitCuf | Number(001,0) | Sim | Situação do Curso |
| PesCuf | Number(002,0) | Sim | Peso do Curso |

---

## Chave Primária

- CodHte
- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077RCF_000

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

### IR_R077RCF_001

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

