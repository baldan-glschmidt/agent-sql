# R083FUN

## Descrição

PPRA - Atividades específicas do colaborador

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador Exposto ao Agente |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador exposto ao agente |
| DatIni | Date | Não | Data de início da atuação do colaborador na atividade |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodAtv | Number(007,0) | Não | Código da Atividade |
| DatTer | Date | Sim | Data de término da atuação do colaborador na atividade |
| DesAte | String(7000) | Sim | Descrição Detalhada |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- TabOrg
- NumLoc
- CodAtv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083FUN_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R083FUN_006

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodAtv | CodAtv |

