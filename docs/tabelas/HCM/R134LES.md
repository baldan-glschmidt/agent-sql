# R134LES

## Descrição

Turmas - Lista de Espera

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 1
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
| SitLes | Number(001,0) | Sim | Indica a Situação do Colaborador na Lista de Espera |
| CodPri | Number(003,0) | Sim | Código de Prioridade do Colaborador |
| DatIns | Date | Sim | Data Inscrição do Colaborador na Lista de Espera |
| HorIns | Number(005,0) | Sim | Hora Inscrição do Colaborador na Lista de Espera |
| OriLes | Number(001,0) | Sim | Origem da Inscrição na Lista de Espera |
| CodUsu | Number(010,0) | Sim | Código Usuário Responsável pela Inscrição |
| TmaCnf | Number(006,0) | Sim | Código da Turma onde foi confirmado a participação |
| SitCon | Number(001,0) | Sim | Define a Situação do Convite |
| DatAce | Date | Sim | Data de Aceite do Convite |
| HorAce | Number(005,0) | Sim | Hora de Aceite do Convite |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad

---

## Índices

### R134LESIndice2

**Tipo:** Não unico

Campos:
- CodCua
- NumEmp
- TipCol
- NumCad
- TmaCnf

---

## Relacionamentos

### IR_R134LES_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134LES_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

