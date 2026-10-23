# R138DCC

## Descrição

Despesas da Turma - Centro de Custo

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCcu | String(018) | Não | Código Centro Custo Contábil |
| CodIdm | Number(003,0) | Sim | Código do Índice |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- CodCcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R138DCC_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R138DCC_002

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

