# R144INT

## Descrição

BS - Instituições Terceiros

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Terceiro |
| CodTip | Number(003,0) | Não | Tipo Instituição |
| CodSer | Number(003,0) | Não | Codigo do Serviço |
| ValSer | Number(008,2) | Sim | Valor do Serviço |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodTip
- CodSer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R144INT_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R144INT_003

**Tabela:** R144TIP

| Origem | Destino |
|--------|---------|
| CodTip | CodTip |

### IR_R144INT_004

**Tabela:** R144SER

| Origem | Destino |
|--------|---------|
| CodSer | CodSer |

