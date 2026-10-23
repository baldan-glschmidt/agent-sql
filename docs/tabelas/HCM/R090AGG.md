# R090AGG

## Descrição

Agendamento de Grupo de Visitantes

---

## Resumo

- Campos: 24
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatPrv | Date | Não | Data Prevista da Visita |
| HorPrv | Number(005,0) | Não | Hora Prevista da Visita |
| NumEmp | Number(004,0) | Não | Código da Empresa do Visitado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador Visitado |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador Visitado |
| SeqAgg | Number(002,0) | Não | Sequência do Agendamento |
| GruVis | Number(003,0) | Sim | Grupo de Visitantes |
| NomGru | String(030) | Sim | Nome do Grupo de Visitantes |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |
| NomOem | String(060) | Sim | Empresa do Grupo de Visitantes |
| QtdVis | Number(003,0) | Sim | Qtde de Visitantes do Grupo |
| TipVis | Number(003,0) | Sim | Tipo de Visita |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso |
| TelCon | String(020) | Sim | Número do Telefone do Grupo para Contato |
| DatVal | Date | Sim | Data da Validade da Visita |
| HorVal | Number(005,0) | Sim | Hora Validade da Visita |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador do Agendamento |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| ObsVis | String(080) | Sim | Observação da Visita |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Agendamento |
| VisEfe | String(001) | Sim | Indica que a Visita foi Efetuada (Agendamento Executado) |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- DatPrv
- HorPrv
- NumEmp
- TipCol
- NumCad
- SeqAgg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090AGG_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

