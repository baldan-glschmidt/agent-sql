# R064LOC

## Descrição

Troca de Local

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data Inicial da Troca de Local |
| HorIni | Number(005,0) | Não | Hora Inicial da Troca de Local |
| DatFim | Date | Sim | Data Final da Troca de Local |
| HorFim | Number(005,0) | Sim | Hora Final da Troca de Local |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| MotAlt | Number(003,0) | Sim | Motivo da Alteração do Local |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064LOC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

