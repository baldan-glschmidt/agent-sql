# R033PHA

## Descrição

Histórico de Cursos de Aperfeiçoamento da Pessoa - Profissionais Responsáveis

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
| CodPes | Number(009,0) | Não | Código da Pessoa |
| SeqCAP | Number(006,0) | Não | Sequência do Curso Aperfeiçoamento |
| SeqPha | Number(004,0) | Não | Sequência do Histórico de Instrutores do Curso |
| CpfPro | Number(011,0) | Sim | CPF do profissional responsável pelo treinamento/capacitação |
| NomPro | String(070) | Sim | Nome do profissional responsável pelo treinamento/capacitação |
| TipPro | Number(001,0) | Sim | Tipo do profissional responsável pelo treinamento/capacitação |
| ForPro | String(255) | Sim | Formação do profissional responsável pelo treinamento/capacitação |
| CodCbo | String(006) | Sim | CBO referente formação do profissional responsável pelo treinamento/capacitação |
| IndNac | Number(001,0) | Sim | Indicativo de nacionalidade |

---

## Chave Primária

- CodPes
- SeqCAP
- SeqPha

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R033PHA_000

**Tabela:** R033PES

| Origem | Destino |
|--------|---------|
| CodPes | CodPes |

