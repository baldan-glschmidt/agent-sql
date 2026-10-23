# R134FRE

## Descrição

Turmas - Controle de Frequência

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Participante |
| NumCad | Number(009,0) | Não | Cadastro do Participante |
| DatPre | Date | Não | Data da Presença |
| CodHcu | Number(006,0) | Não | Código do Horário |
| TmaFre | Number(006,0) | Sim | Código da Turma Frequentada |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad
- DatPre
- CodHcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134FRE_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134FRE_006

**Tabela:** R133HCU

| Origem | Destino |
|--------|---------|
| CodHcu | CodHcu |

