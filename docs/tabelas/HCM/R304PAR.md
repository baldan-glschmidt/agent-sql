# R304PAR

## Descrição

e-Sfinge Online - Parecer do Controle Interno

---

## Resumo

- Campos: 18
- Chave Primária: 8 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| NumAto | String(016) | Não | Número do Ato que Admitiu ou Nomeou o Servidor |
| NumMat | String(016) | Não | Número da Matrícula do Servidor na Unidade |
| TipPar | Number(002,0) | Não | Tipo de Parecer do CI |
| TipAto | Number(002,0) | Não | Tipo de Ato |
| SeqReg | Number(009,0) | Não | Sequência |
| PidSta | String(030) | Sim | Pid Status |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(008,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(008,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(008,0) | Sim | Campo Auxiliar 5 |
| CmpAu6 | Number(008,0) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(002) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(002) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(2000) | Sim | Campo Auxiliar 9 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- NumAto
- NumMat
- TipPar
- TipAto
- SeqReg

---

## Índices

### R304PARIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

### IR_R304PAR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

