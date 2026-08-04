# E803TRB

## Descrição

PCP - Dados do Turno de Trabalho

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodEtg | Number(004,0) | Não | Estágio de Produção onde o Recurso é Utilizado |
| CodCre | String(008) | Não | Código do Centro de Recurso (conjunto Máquina/Pessoa c/ mesma capacidade produtiva) |
| TurTrb | Number(001,0) | Não | Turno de Trabalho |
| DatVal | Date | Não | Data Validade (Até) desta informação p/ este Turno |
| QtdHor | Number(004,2) | Sim | Quantidade  de horas/dia NORMAIS no Turno, trabalhadas no Centro de Recursos específico |
| PerDia | Number(006,3) | Sim | Percentual de horas/dia no Turno de trabalho em relação ao total de Horas do C. Recursos do Estágio |
| DatAlt | Date | Sim | Data da Alteração |
| HorAlt | Number(005,0) | Sim | Hora da alteração |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Alterou |
| ItvSab | String(001) | Não | Tem intervalos para os Sábados |
| ItvDom | String(001) | Não | Tem intervalos para os Domingos |
| ItvFer | String(001) | Não | Tem intervalos para os Feriados |

---

## Chave Primária

- CodEmp
- CodEtg
- CodCre
- TurTrb
- DatVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
