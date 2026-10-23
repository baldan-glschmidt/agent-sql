# R064SOB

## Descrição

Sobreaviso ou Prontidão

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Programação de Sobreaviso ou Prontidão |
| HorIni | Number(005,0) | Não | Hora Inicial da Programação de Sobreaviso ou Prontidão |
| DatFim | Date | Sim | Data Final da Programação de Sobreaviso ou Prontidão |
| HorFim | Number(005,0) | Sim | Hora Final da Programação de Sobreaviso ou Prontidão |
| CodSit | Number(003,0) | Sim | Código da Situação de Sobreaviso ou Prontidão |
| ObsSob | String(100) | Sim | Observação de Sobreaviso ou Prontidão |
| SobCon | String(001) | Sim | Contínuo |

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

### IR_R064SOB_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R064SOB_007

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

