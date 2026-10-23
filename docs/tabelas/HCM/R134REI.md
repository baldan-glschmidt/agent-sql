# R134REI

## Descrição

Turmas - Recursos Instrucionais

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodRei | Number(004,0) | Não | Código do Recurso Instrucional |
| QtdRei | Number(004,0) | Sim | Quantidade de Recursos Instrucionais |

---

## Chave Primária

- CodCua
- TmaCua
- CodRei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134REI_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134REI_002

**Tabela:** R140REI

| Origem | Destino |
|--------|---------|
| CodRei | CodRei |

