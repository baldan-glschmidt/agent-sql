# R134COM

## Descrição

Turmas - Comentário/Participantes

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo Colaborador Participante |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Participante |
| ComPos | String(1600) | Sim | Comentário Positivo do Participante sobre o Curso |
| ComNeg | String(1600) | Sim | Comentário Negativo do Participante sobre o Curso |
| ComPIn | String(1600) | Sim | Comentário positivo do instrutor sobre o participante |
| ComNIn | String(1600) | Sim | Comentário negativo do instrutor sobre o participante |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134COM_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134COM_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

