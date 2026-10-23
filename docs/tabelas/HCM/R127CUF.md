# R127CUF

## Descrição

Cursos de Formação

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCuf | Number(004,0) | Não | Código do Curso de Formação |
| NomRed | String(030) | Sim | Nome Reduzido Curso |
| NomCuf | String(060) | Sim | Nome do Curso |
| NivCuf | Number(002,0) | Sim | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Sim | Sequência do Nível |
| CodAss | Number(004,0) | Sim | Código do Assunto |
| TipDur | Number(001,0) | Sim | Tipo de Duração |
| TemDur | Number(003,0) | Sim | Tempo de Duração |
| ChrCuf | Number(010,0) | Sim | Carga Horária |
| ConWeb | String(001) | Sim | Considerar no preenchimento do Currículo Web |

---

## Chave Primária

- CodCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127CUF_005

**Tabela:** R128ASS

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |

