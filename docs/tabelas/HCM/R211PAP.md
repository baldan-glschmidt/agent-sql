# R211PAP

## Descrição

Pesquisa - Definição - Participantes

---

## Resumo

- Campos: 7
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPsq | Number(006,0) | Não | Código da Pesquisa |
| SeqPsq | Number(002,0) | Não | Sequência da pesquisa |
| SeqPap | Number(005,0) | Não | Sequência do Participante |
| NumEmp | Number(004,0) | Não | Código da Empresa do Participante |
| TipCol | Number(001,0) | Não | Tipo Colaborador Participante |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Participante |
| SeqIde | Number(005,0) | Sim | Sequência da identificação |

---

## Chave Primária

- CodPsq
- SeqPsq
- SeqPap
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R211PAP_001

**Tabela:** R211DEF

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |
| SeqPsq | SeqPsq |

