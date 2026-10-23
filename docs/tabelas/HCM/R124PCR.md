# R124PCR

## Descrição

Colaborador - Cursos Aperfeiçoamento - Profissionais Responsáveis

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodCua | Number(009,0) | Não | Código do Curso |
| SeqHcr | Number(004,0) | Não | Sequência do Curso Aperfeiçoamento |
| SeqPcr | Number(004,0) | Não | Sequência do Histórico de Instrutores do Curso |
| CpfPro | Number(011,0) | Sim | CPF do profissional responsável pelo treinamento/capacitação |
| NomPro | String(070) | Sim | Nome do profissional responsável pelo treinamento/capacitação |
| TipPro | Number(001,0) | Sim | Tipo do profissional responsável pelo treinamento/capacitação |
| ForPro | String(255) | Sim | Formação do profissional responsável pelo treinamento/capacitação |
| CodCbo | String(006) | Sim | CBO referente formação do profissional responsável pelo treinamento/capacitação |
| IndNac | Number(001,0) | Sim | Indicativo de nacionalidade |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCua
- SeqHcr
- SeqPcr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124PCR_003

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

