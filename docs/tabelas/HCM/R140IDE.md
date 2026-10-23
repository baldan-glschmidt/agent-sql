# R140IDE

## Descrição

Avaliação de Reação - Identificadores

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código Curso |
| TmaCua | Number(006,0) | Não | Código Turma |
| SeqIde | Number(005,0) | Não | Sequência da identificação |
| IdePar | String(024) | Sim | Identificação do Participante na Avaliação de Reação |
| SeqAno | Number(004,0) | Sim | Sequência que individualiza o anônimo |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador Participante |
| NumCad | Number(009,0) | Sim | Participante |
| AvRCon | String(001) | Sim | Avaliação de Reação Concluída |

---

## Chave Primária

- CodCua
- TmaCua
- SeqIde

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140IDE_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

