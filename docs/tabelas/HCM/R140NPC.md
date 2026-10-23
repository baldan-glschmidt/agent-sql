# R140NPC

## Descrição

Frequência do Participante

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Não | Código da Turma |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Participante |
| NumCad | Number(009,0) | Não | Cadastro do Participante |
| QtdFal | Number(003,0) | Sim | Quantidade de Faltas |
| HorFal | Number(010,0) | Sim | Horas Faltas |
| TipCer | String(001) | Sim | Tipo do Certificado |
| NumCer | Number(005,0) | Sim | Número do Certificado |
| SitCua | Number(002,0) | Sim | Situação Histórico Curso Aperfeiçoamento |
| CodMin | Number(003,0) | Sim | Código do motivo de interrupção |
| SitARe | Number(001,0) | Sim | Situação da Avaliação de Reação |
| SitAnt | Number(002,0) | Sim | Situação Anterior do Histórico Curso Aperfeiçoamento - Turma Cancelada |

---

## Chave Primária

- CodCua
- TmaCua
- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R140NPC_001

**Tabela:** R134DTU

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |
| TmaCua | TmaCua |

