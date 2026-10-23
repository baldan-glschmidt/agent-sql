# R134CNV

## Descrição

Turmas - Convênios

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
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| CodOem | Number(008,0) | Não | Código da Outra Empresa Conveniada |
| PerOem | Number(005,2) | Sim | Percentual do Convênio |
| CodIdm | Number(003,0) | Sim | Código do Índice |
| ValOem | Number(011,2) | Sim | Valor do Convênio |

---

## Chave Primária

- CodCua
- TmaCua
- CodOem

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134CNV_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134CNV_002

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

