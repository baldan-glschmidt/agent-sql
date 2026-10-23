# R011TBH

## Descrição

Totalizador Banco de Horas

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodBHr | Number(005,0) | Não | Código do Banco de Horas |
| PerRef | Date | Não | Competência do Cálculo |
| QtdPag | Number(010,0) | Não | Horas a Pagar |
| QtdDes | Number(010,0) | Não | Horas a Descontar |
| QtdSal | Number(010,0) | Não | Saldo |
| ValPag | Number(013,4) | Não | Valor Horas a Pagar |
| ValDes | Number(013,4) | Não | Valor Horas a Descontar |
| ValSal | Number(013,4) | Não | Valor Horas do Saldo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBHr
- PerRef

---

## Índices

### R011TBHIndice1

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- PerRef

---

## Relacionamentos

### IR_R011TBH_003

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBHr | CodBHr |

