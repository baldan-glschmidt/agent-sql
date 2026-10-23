# R128TES

## Descrição

Cursos Aperfeiçoamento - Testes Turma

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
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| CodTst | String(005) | Não | Código do Teste |
| QtdPer | Number(003,0) | Sim | Quantidade de Perguntas do Teste |

---

## Chave Primária

- CodCua
- CodTst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128TES_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R128TES_001

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

