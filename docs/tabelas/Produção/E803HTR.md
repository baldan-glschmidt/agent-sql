# E803HTR

## Descrição

PCP - Horários do Turno de Trabalho

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodEtg | Number(004,0) | Não | Estágio de Produção onde o Recurso é Utilizado |
| CodCre | String(008) | Não | Código do Centro de Recurso (Quando Turno Específico) |
| TurTrb | Number(001,0) | Não | Turno de Trabalho |
| DatVal | Date | Não | Data Validade (Até) desta informação p/ este Turno |
| SeqHtr | Number(004,0) | Não | Ordem sequencial dos horários de Trabalhos dos Turnos (Início e Fim) |
| HorIni | Number(005,0) | Sim | Início do Horário de trabalho (início do expediente/intervalo) |
| HorFim | Number(005,0) | Sim | Fim do Horário de trabalho(fim do expediente/intervalo) |
| DatAlt | Date | Sim | Data da Alteração |
| HorAlt | Number(005,0) | Sim | Hora da alteração |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Alterou |
| TipHtr | String(001) | Não | Tipo de Intervalo de trabalho (p/ Sábados, Domingos, Feriados ou dias Normais) |

---

## Chave Primária

- CodEmp
- CodEtg
- CodCre
- TurTrb
- DatVal
- SeqHtr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
