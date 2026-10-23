# R041MAP

## Descrição

Aposentadoria - Mestre

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| DatApo | Date | Sim | Data Aposentadoria |
| CodReg | Number(003,0) | Sim | Código da Regra |
| CodVin | Number(002,0) | Sim | Vínculo p/ Aposentadoria |
| TipApo | Number(001,0) | Sim | Tipo da Aposentadoria |
| PerSal | Number(005,2) | Sim | Percentual Salário |
| ProPor | Number(005,2) | Sim | Proporcionalidade Percentual |
| ProAvo | Number(005,2) | Sim | Proporcionalidade Avos |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R041MAP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R041MAP_004

**Tabela:** R041REG

| Origem | Destino |
|--------|---------|
| CodReg | CodReg |

