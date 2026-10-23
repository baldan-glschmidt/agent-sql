# R134DCL

## Descrição

Calendário Cursos Treinamento - Definição

---

## Resumo

- Campos: 17
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| DatCua | Date | Não | Data do Curso |
| SeqCua | Number(002,0) | Não | Sequência do Curso p/ Mesma Data |
| DatFim | Date | Sim | Data de Término |
| QtdAul | Number(003,0) | Sim | Quantidade de Aulas |
| TipDur | Number(001,0) | Sim | Tipo de Duração |
| TemDur | Number(003,0) | Sim | Tempo Duração |
| CarHor | Number(010,0) | Sim | Carga Horária |
| QtdVag | Number(006,0) | Sim | Quantidade de Vagas |
| TipCur | Number(001,0) | Sim | Tipo Realização |
| EndCua | String(040) | Sim | Endereço da Realização Curso |
| CodSla | Number(004,0) | Sim | Código da Sala de Treinamento |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| CodBai | Number(004,0) | Sim | Código do Bairro |
| CodCep | Number(008,0) | Sim | CEP |
| CodFes | Number(008,0) | Sim | Código da Entidade de Treinamento |
| TmaCua | Number(006,0) | Sim | Código da Turma relacionada ao calendário |

---

## Chave Primária

- CodCua
- DatCua
- SeqCua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R134DCL_000

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

