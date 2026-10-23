# R140DLI

## Descrição

Ocupação Extraordinária - Despesas - Item de Custo

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSla | Number(004,0) | Não | Código da Sala de Treinamento |
| DatOcu | Date | Não | Data Ocupação da Sala |
| HorIni | Number(005,0) | Não | Hora Início da Ocupação |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | lookup para tabela de organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodTcu | Number(004,0) | Não | Item Custo |
| ValCus | Number(011,2) | Sim | Valor do Ítem |

---

## Chave Primária

- CodSla
- DatOcu
- HorIni
- NumEmp
- TabOrg
- NumLoc
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140DLI_000

**Tabela:** R140SLA

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |

### IR_R140DLI_002

**Tabela:** R140SOC

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |
| DatOcu | DatOcu |
| HorIni | HorIni |

### IR_R140DLI_005

**Tabela:** R140DLL

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |
| DatOcu | DatOcu |
| HorIni | HorIni |
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R140DLI_006

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

