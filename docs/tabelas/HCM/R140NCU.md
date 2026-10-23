# R140NCU

## Descrição

Notas do Curso

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código Curso |
| TmaCua | Number(006,0) | Não | Código Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador Participante |
| NumCad | Number(009,0) | Não | Participante |
| CodTnt | Number(003,0) | Não | Item de Nota do Curso |
| NotCur | Number(005,2) | Sim | Nota do Curso |
| ObsCur | String(500) | Sim | Observação sobre a nota do curso |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad
- CodTnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140NCU_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R140NCU_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R140NCU_005

**Tabela:** R140NTR

| Origem | Destino |
|--------|---------|
| CodTnt | CodTnt |

