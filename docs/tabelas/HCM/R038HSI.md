# R038HSI

## Descrição

Histórico Sindicato

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do Sindicato |
| CodSin | Number(004,0) | Sim | Código do Sindicato |
| SocSin | String(001) | Sim | Sócio do Sindicato |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| PossBH | String(001) | Sim | Possui banco de horas |
| UsaBhr | Number(001,0) | Sim | Utiliza Banco de Horas |
| CodBHr | Number(005,0) | Sim | Código do Banco de Horas |
| TraBHr | Number(001,0) | Sim | Tratar banco de horas |
| CodBhD | Number(005,0) | Sim | Banco de horas destino |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HSIIndice2

**Tipo:** Não unico

Campos:
- CodSin

---

## Relacionamentos

### IR_R038HSI_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

