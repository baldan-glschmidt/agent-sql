# R070MES

## Descrição

Histórico de Crachás Mestre

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Responsável pelo Crachá Mestre |
| DatIni | Date | Não | Data de Início do Uso do Crachá |
| HorIni | Number(005,0) | Não | Hora de Início do Uso do Crachá |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatFim | Date | Sim | Data Final do Uso do Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Uso do Crachá |
| StaAtu | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

### R070MESIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatIni
- HorIni

---

## Relacionamentos

### IR_R070MES_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

