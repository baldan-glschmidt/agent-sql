# R127FAS

## Descrição

Cursos de Formação - Fases

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NivCuf | Number(002,0) | Não | Nível de Formação do Curso |
| SeqNiv | Number(002,0) | Não | Sequência do Nível |
| FasCuf | String(003) | Não | Fase do Curso de Formação |
| DesFas | String(030) | Sim | Descrição da Fase |
| GinCpl | Number(002,0) | Sim | Código do Grau de Instrução para Curso Completo |
| GinInc | Number(002,0) | Sim | Código do Grau de Instrução para Curso Incompleto |

---

## Chave Primária

- NivCuf
- SeqNiv
- FasCuf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R127FAS_004

**Tabela:** R022GRA

| Origem | Destino |
|--------|---------|
| GinCpl | GraIns |

### IR_R127FAS_005

**Tabela:** R022GRA

| Origem | Destino |
|--------|---------|
| GinInc | GraIns |

