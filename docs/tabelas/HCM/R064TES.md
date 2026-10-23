# R064TES

## Descrição

Troca de Escala

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data Inicial da Troca de Escala |
| DatFim | Date | Sim | Data Final da Troca de Escala |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodTma | Number(001,0) | Sim | Código da Turma |
| TurInt | Number(009,0) | Sim | Código da Turma de Intervalo |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| CodEqp | Number(004,0) | Sim | Código da Equipe |
| CodCat | Number(003,0) | Sim | Código da Categoria |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R064TES_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R064TES_005

**Tabela:** R006ESC

| Origem | Destino |
|--------|---------|
| CodEsc | CodEsc |

