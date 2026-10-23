# R122CCF

## Descrição

Candidatos Externos - Cursos de Formação

---

## Resumo

- Campos: 17
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| CodCuf | Number(004,0) | Não | Código do Curso |
| SeqCcf | Number(002,0) | Não | Sequência Curso de Formação |
| PerIni | Date | Sim | Data Início |
| PerFim | Date | Sim | Data Fim |
| CodOem | Number(008,0) | Sim | Código Entidade |
| NomOem | String(060) | Sim | Nome da entidade de ensino |
| SitCuf | Number(002,0) | Sim | Situação Curso |
| NivCuf | Number(002,0) | Sim | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Sim | Sequência do Nível |
| FasCuf | String(003) | Sim | Fase do Curso de Formação |
| ComCuf | String(250) | Sim | Comentário Formação Curso |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |
| NomCuf | String(060) | Sim | Nome do Curso |
| SeqCFP | Number(006,0) | Sim | Sequência do Curso Formação |
| OriInf | Number(001,0) | Sim | Origem da informação do curso |
| USU_NomCurso | String(060) | Sim | OUTROS CURSOS |

---

## Chave Primária

- NumCan
- CodCuf
- SeqCcf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CCF_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CCF_001

**Tabela:** R127CUF

| Origem | Destino |
|--------|---------|
| CodCuf | CodCuf |

