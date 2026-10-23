# R134EDR

## Descrição

Turmas - Exceção Participantes

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
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
| CodHcu | Number(006,0) | Não | Código do Horário Curso |
| DatExc | Date | Não | Data da Exceção |
| HorIni | Number(005,0) | Não | Hora Início da Exceção |
| HorTer | Number(005,0) | Sim | Hora Término da Exceção |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad
- CodHcu
- DatExc
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134EDR_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134EDR_004

**Tabela:** R134DRE

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

