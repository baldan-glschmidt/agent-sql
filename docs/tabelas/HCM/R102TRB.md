# R102TRB

## Descrição

Trabalhos do SESMT - Participantes

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodTbr | Number(006,0) | Não | Código do Trabalho |
| EmpPar | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador Participante |
| SeqReg | Number(002,0) | Não | Sequência da participação |
| CodBri | Number(003,0) | Sim | Código da Brigada |
| ObsPar | String(1500) | Sim | Observação do Participante |
| ParRes | String(001) | Sim | Define se o participante é responsável |

---

## Chave Primária

- NumEmp
- CodTbr
- EmpPar
- TipCol
- NumCad
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R102TRB_001

**Tabela:** R102TBR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodTbr | CodTbr |

### IR_R102TRB_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| EmpPar | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

