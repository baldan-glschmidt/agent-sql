# R130DCU

## Descrição

Despesas da Turma - Curso

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodIdm | Number(003,0) | Sim | Código do Índice |

---

## Chave Primária

- CodCua
- TmaCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130DCU_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

