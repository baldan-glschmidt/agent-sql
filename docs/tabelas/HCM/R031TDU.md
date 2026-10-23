# R031TDU

## Descrição

Geração de Escalas - Programação de Turno Duplo

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DiaPrf | Date | Não | Data Alteração |
| CodEqp | Number(004,0) | Sim | Código da Equipe |
| CodTur | Number(001,0) | Sim | Código do Turno |
| CodCat | Number(003,0) | Sim | Código da Categoria |
| CodHor | Number(004,0) | Sim | Código do Horário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DiaPrf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R031TDU_007

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

