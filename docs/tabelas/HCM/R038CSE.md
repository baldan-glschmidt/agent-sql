# R038CSE

## Descrição

Histórico de Composição Salarial - Eventos

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CmpAlt | Date | Não | Competência de Alteração |
| CodTab | Number(003,0) | Não | Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodMot | Number(003,0) | Sim | Código do Motivo da Alteração |
| ValSal | Number(013,4) | Sim | Valor Salário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAlt
- CodTab
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038CSE_004

**Tabela:** R008EVM

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |

### IR_R038CSE_005

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

