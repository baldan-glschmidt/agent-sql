# R123RCA

## Descrição

Requisições - Requisitos Cursos Aperfeiçoamento - Temporária

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código da Requisição |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| IndVal | String(001) | Sim | Define se o requisito deve ser considerado na triagem/seletiva |
| EqvTri | Number(004,0) | Sim | Grupo de Equivalência Específica para Triagem/Seletiva |
| PtsRca | Number(002,0) | Sim | Pontuação do Curso de Aperfeiçoamento |

---

## Chave Primária

- CodRqu
- CodCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R123RCA_001

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

