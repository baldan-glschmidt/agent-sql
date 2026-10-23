# R184OCO

## Descrição

PLR - Objetivos do Colaborador

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| CmpPpr | Date | Não | Competência de Cálculo do PPR |
| CodObj | Number(004,0) | Não | Código do Objetivo |
| DatIni | Date | Sim | Data Início da Validade do Objetivo |
| DatFim | Date | Sim | Data Final da Validade do Objetivo |
| PesObj | Number(011,2) | Sim | Peso do Objetivo |
| SinObj | String(001) | Sim | Sinal de Operação (Soma ou Subtração) |
| SomPon | String(001) | Sim | Soma para Pontuação do Colaborador |
| CodFlt | Number(003,0) | Sim | Código Regra |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpPpr
- CodObj

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R184OCO_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R184OCO_003

**Tabela:** R182DEF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpr | CmpPpr |

### IR_R184OCO_004

**Tabela:** R182OBJ

| Origem | Destino |
|--------|---------|
| CodObj | CodObj |

