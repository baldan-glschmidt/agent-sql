# R132REC

## Descrição

Reserva de curso - Agrupada por competência - Participantes

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCua | Number(009,0) | Não | Código do Curso |
| CmpRea | Date | Não | Competência da Realização |
| SeqTre | Number(002,0) | Não | Sequência da Reserva |
| EmpPar | Number(004,0) | Não | Código Empresa do Participante da Reserva |
| TipPar | Number(001,0) | Não | Tipo de Colaborador Participante Reserva |
| CadPar | Number(009,0) | Não | Cadastro do Colaborador Participante Reserva |
| TmaCua | Number(006,0) | Sim | Código Turma |
| ObsPar | String(020) | Sim | Observação do Participante |
| CmpAva | Date | Sim | Competência da Avaliação |
| SeqAva | Number(004,0) | Sim | Sequência da Avaliação |
| CodEvn | Number(009,0) | Sim | Código do Evento |

---

## Chave Primária

- NumEmp
- CodCua
- CmpRea
- SeqTre
- EmpPar
- TipPar
- CadPar

---

## Índices

### R132RECIndice2

**Tipo:** Não unico

Campos:
- CodCua
- EmpPar
- TipPar
- CadPar
- TmaCua

---

## Relacionamentos

### IR_R132REC_003

**Tabela:** R132RES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCua | CodCua |
| CmpRea | CmpRea |
| SeqTre | SeqTre |

### IR_R132REC_006

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpPar | NumEmp |
| TipPar | TipCol |
| CadPar | NumCad |

