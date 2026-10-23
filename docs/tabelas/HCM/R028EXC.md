# R028EXC

## Descrição

Exceções Vale Transporte

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data de Início das Exceções Vale Transporte |
| CodLin | Number(005,0) | Não | Código da Linha |
| PasUte | Number(002,0) | Sim | Qtde de Passes em Dias Úteis |
| PasSab | Number(002,0) | Sim | Qtde de Passes aos Sábados |
| PasDom | Number(002,0) | Sim | Qtde de Passes aos Domingos |
| PasFer | Number(002,0) | Sim | Qtde de Passes em Feriados |
| PasFix | Number(003,0) | Sim | Qtde de Passes Fixos |
| PasSeg | Number(002,0) | Sim | Qtde de Passes às Segundas |
| PasTer | Number(002,0) | Sim | Qtde de Passes às Terças |
| PasQua | Number(002,0) | Sim | Qtde de Passes às Quartas |
| PasQui | Number(002,0) | Sim | Qtde de Passes às Quintas |
| PasSex | Number(002,0) | Sim | Qtde de Passes às Sextas |
| DatFim | Date | Sim | Data Final da Exceção de Vale Transporte |
| PasFol | Number(002,0) | Sim | Qtde de Passes em Folga |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- CodLin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R028EXC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R028EXC_004

**Tabela:** R028LVT

| Origem | Destino |
|--------|---------|
| CodLin | CodLin |

