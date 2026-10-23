# R211LID

## Descrição

Pesquisa - Definição - Líder avaliado

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPsq | Number(006,0) | Não | Código da Pesquisa |
| SeqPsq | Number(002,0) | Não | Sequência da pesquisa |
| SeqPap | Number(005,0) | Não | Sequência do líder |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Líder |
| TipCol | Number(001,0) | Sim | Tipo Colaborador Líder |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Líder |
| PerLid | Number(005,2) | Sim | % atingido na pesquisa sobre atendimento das necessidades dos liderados |

---

## Chave Primária

- CodPsq
- SeqPsq
- SeqPap

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211LID_000

**Tabela:** R211PSQ

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |

### IR_R211LID_001

**Tabela:** R211DEF

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |
| SeqPsq | SeqPsq |

