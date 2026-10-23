# R040INV

## Descrição

Recibo de Férias - Dias Inválidos

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| IniPer | Date | Não | Início do período aquisitivo |
| IniFer | Date | Não | Início das férias |
| DatInv | Date | Não | Data que não deve ser considerada como férias |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- IniFer
- DatInv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R040INV_003

**Tabela:** R040PER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |

### IR_R040INV_004

**Tabela:** R040FEM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |
| IniFer | IniFer |

