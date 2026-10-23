# R128REV

## Descrição

Cursos Aperfeiçoamento - Revisões do Curso

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
| DatAlt | Date | Não | Data da Revisão |
| ObsRev | String(1000) | Sim | Observações |

---

## Chave Primária

- CodCua
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128REV_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

