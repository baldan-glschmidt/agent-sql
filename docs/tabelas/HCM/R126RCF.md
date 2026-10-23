# R126RCF

## Descrição

Requisições - Requisitos Cursos Formação

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código da Requisição |
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| SitCuf | Number(001,0) | Sim | Situação do Curso |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| EqvTri | Number(004,0) | Sim | Grupo de Equivalência Específica para Triagem/Seletiva |
| PtsRcf | Number(002,0) | Sim | Pontuação do Curso de Formação |

---

## Chave Primária

- CodRqu
- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126RCF_000

**Tabela:** R126RQU

| Origem | Destino |
|--------|---------|
| CodRqu | CodRqu |

### IR_R126RCF_001

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

