# R134INS

## Descrição

Turmas - Instrutores

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa do Instrutor |
| TipCol | Number(001,0) | Não | Tipo do Instrutor |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador do Instrutor |
| ObsIns | String(500) | Sim | Dados complementares do instrutor |
| TipIns | Number(001,0) | Sim | Indica se o colaborador é instrutor, avaliador ou ambos |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad

---

## Índices

### R134INSIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

### IR_R134INS_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134INS_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

