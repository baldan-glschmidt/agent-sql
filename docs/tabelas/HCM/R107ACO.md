# R107ACO

## Descrição

PDI - Reuniões de acompanhamento do plano de desenvolvimento

---

## Resumo

- Campos: 17
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| CodPln | Number(004,0) | Não | Código do Plano de Desenvolvimento |
| CodObj | Number(002,0) | Não | Código do Objetivo |
| CodAco | Number(002,0) | Não | Código da Ação |
| SeqAco | Number(002,0) | Não | Sequência da Ação |
| DatAco | Date | Sim | Data do Acompanhamento |
| AndAco | String(200) | Sim | Andamento da Ação |
| NotAco | Number(006,2) | Sim | Nota |
| DesRes | String(500) | Sim | Descrição do Resultado |
| PerAco | Number(005,2) | Sim | % Realizado |
| ProEnc | Date | Sim | Data do próximo encontro |
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Sim | Código da Turma |
| CodEvn | Number(009,0) | Sim | Código do Evento |
| UsuAco | Number(009,0) | Sim | Usuário que criou o acompanhamento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPln
- CodObj
- CodAco
- SeqAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
