# R038HPP

## Descrição

Histórico Assinalamento PPR

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatAlt | Date | Não | Data da Alteração |
| AssPpr | Number(001,0) | Sim | Assinalamento do Colaborador p/ PPR |
| StaHis | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HPPIndice2

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

---

## Relacionamentos

### IR_R038HPP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

