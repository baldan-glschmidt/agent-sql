# R090MGV

## Descrição

Entrada/Saída de Grupo de Visitantes

---

## Resumo

- Campos: 27
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatEnt | Date | Não | Data de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Visitado |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador Visitado |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Visitado |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodPor | Number(003,0) | Sim | Código da Portaria da Entrada do Grupo |
| GruVis | Number(003,0) | Sim | Grupo de Visitantes |
| NomGru | String(030) | Sim | Nome do Grupo de Visitantes |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |
| NomOem | String(060) | Sim | Empresa do Grupo de Visitantes |
| CodPrm | Number(005,0) | Sim | Permissão de Acesso |
| TelCon | String(020) | Sim | Número do Telefone do Grupo para Contato |
| DatVal | Date | Sim | Data da Validade da Visita |
| HorVal | Number(005,0) | Sim | Hora Validade da Visita |
| QtdVis | Number(003,0) | Sim | Qtde de Visitantes do Grupo |
| TipVis | Number(003,0) | Sim | Tipo de Visita |
| ObsVis | String(080) | Sim | Observação da Visita |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou a Entrada |
| DatSai | Date | Sim | Data da Saída do Grupo do Local Visitado |
| HorSai | Number(005,0) | Sim | Hora da Saída do Grupo |
| DatSLo | Date | Sim | Data da Saída da Portaria da Empresa |
| HorSLo | Number(005,0) | Sim | Hora da Saída da Portaria da Empresa |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |

---

## Chave Primária

- DatEnt
- HorEnt
- SeqEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
