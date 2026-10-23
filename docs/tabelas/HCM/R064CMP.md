# R064CMP

## Descrição

Compensações

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data Inicial da Compensação |
| TipCmp | Number(001,0) | Não | Tipo da Compensação |
| PerCmp | Number(001,0) | Não | Período da Compensação |
| DatFim | Date | Sim | Data Final Compensação |
| IniInt | Number(005,0) | Sim | Início Intervalo |
| FimInt | Number(005,0) | Sim | Fim Intervalo |
| QtdHor | Number(005,0) | Sim | Qtde de Horas da Compensação |
| CodSit | Number(003,0) | Sim | Código da Situação da Compensação |
| MotSit | Number(003,0) | Sim | Motivo da Situação |
| CodHor | Number(004,0) | Sim | Código do Horário da Compensação |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- TipCmp
- PerCmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064CMP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

