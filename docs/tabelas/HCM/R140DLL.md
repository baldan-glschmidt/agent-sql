# R140DLL

## Descrição

Ocupação Extraordinária - Despesas

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

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
| CodIdm | Number(003,0) | Sim | Código do Índice |

---

## Chave Primária

- CodSla
- DatOcu
- HorIni
- NumEmp
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140DLL_000

**Tabela:** R140SLA

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |

### IR_R140DLL_002

**Tabela:** R140SOC

| Origem | Destino |
|--------|---------|
| CodSla | CodSla |
| DatOcu | DatOcu |
| HorIni | HorIni |

