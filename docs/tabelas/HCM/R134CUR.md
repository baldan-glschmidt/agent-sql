# R134CUR

## Descrição

Turmas Modular - Histórico Participante

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
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
| CodCur | Number(009,0) | Não | Código do curso do histórico |
| SeqHcr | Number(004,0) | Sim | Sequência do curso aperfeiçoamento cfe histórico |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad
- CodCur

---

## Índices

### R134CURIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- CodCur
- SeqHcr

---

## Relacionamentos

### IR_R134CUR_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

### IR_R134CUR_005

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCur | CodCua |

