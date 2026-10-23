# R088SOL

## Descrição

Solicitação de Veículos

---

## Resumo

- Campos: 22
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSol | Number(006,0) | Não | Código da Solicitação de Uso de Veículo |
| DatSol | Date | Sim | Data da Solicitação do Veículo |
| HorSol | Number(005,0) | Sim | Hora da Solicitação do Veículo |
| TipVei | Number(002,0) | Sim | Tipo de Veículo e Espécie Contram |
| EmpSol | Number(004,0) | Sim | Código da Empresa do Solicitante da Solicitação |
| TipSol | Number(001,0) | Sim | Tipo do Solicitante |
| CadSol | Number(009,0) | Sim | Cadastro do Solicitante |
| SolCon | String(001) | Sim | Solicitante será Condutor. |
| MotUso | Number(003,0) | Sim | Motivo Uso do Veículo |
| DesVei | String(040) | Sim | Local de Destino do Veículo |
| DatUso | Date | Sim | Data do Agendamento do Veículo |
| HorUso | Number(005,0) | Sim | Hora do Agendamento do Veículo |
| DatPrv | Date | Sim | Data Prevista para Retorno |
| HorPrv | Number(005,0) | Sim | Hora Prevista para Retorno |
| DatVal | Date | Sim | Data da Validade da Solicitação |
| HorVal | Number(005,0) | Sim | Hora da Validade da Solicitação |
| EmpApr | Number(004,0) | Sim | Código da Empresa do Aprovador da Solicitação |
| TipApr | Number(001,0) | Sim | Tipo Aprovador da Solicitação |
| CadApr | Number(009,0) | Sim | Cadastro do Aprovador da Solicitação |
| DatApr | Date | Sim | Data da Aprovação da Solicitação do Veículo |
| HorApr | Number(005,0) | Sim | Hora Aprovação da Solicitação do Veículo |
| StaSol | Number(001,0) | Sim | Status Solicitação |

---

## Chave Primária

- CodSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088SOL_003

**Tabela:** R088TPV

| Origem | Destino |
|--------|---------|
| TipVei | TipTpv |

