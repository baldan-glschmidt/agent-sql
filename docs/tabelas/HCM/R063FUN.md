# R063FUN

## Descrição

Vigilantes

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| CodRon | Number(003,0) | Não | Código da Ronda |
| DatIni | Date | Não | Data Inicial |
| DatFim | Date | Sim | Data Final |
| StaAtu | Number(001,0) | Sim | Status do Histórico |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodRon
- DatIni

---

## Índices

### R063FUNIndice2

**Tipo:** Não unico

Campos:
- CodRon
- DatIni
- DatFim

---

## Relacionamentos

### IR_R063FUN_003

**Tabela:** R063RON

| Origem | Destino |
|--------|---------|
| CodRon | CodRon |

