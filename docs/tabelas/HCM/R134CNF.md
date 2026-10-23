# R134CNF

## Descrição

Turmas - Confirma Participantes

---

## Resumo

- Campos: 8
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EmpPar | Number(004,0) | Não | Código da Empresa do Participante |
| TipPar | Number(001,0) | Não | Tipo de Colaborador Participante |
| CadPar | Number(009,0) | Não | Cadastro do Colaborador Participante |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TabOrg
- NumLoc
- EmpPar
- TipPar
- CadPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134CNF_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134CNF_004

**Tabela:** R134DTL

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R134CNF_007

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpPar | NumEmp |
| TipPar | TipCol |
| CadPar | NumCad |

