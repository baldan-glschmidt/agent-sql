# R104SEN

## Descrição

JR - Sentença - Trabalhista

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CodTab | Number(003,0) | Não | Código da Tabela Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| PerIni | Date | Não | Período de início do direito |
| PerFim | Date | Sim | Período de fim de direito |
| ValEve | Number(011,2) | Sim | Valor do evento |

---

## Chave Primária

- NumEmp
- CodPrc
- EmpAut
- TipCol
- NumCad
- CodTab
- CodEve
- PerIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104SEN_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

### IR_R104SEN_006

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| CodTab | CodTab |
| CodEve | CodEve |

