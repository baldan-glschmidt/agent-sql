# R088AGN

## Descrição

Agendamento de Manutenção de Veículo

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatAgm | Date | Não | Data do Agendamento da Manutenção |
| HorAgm | Number(005,0) | Não | Hora de Agendamento da Manutenção |
| DatPrv | Date | Sim | Data prevista de retorno de manutenção |
| HorPrv | Number(005,0) | Sim | Hora prevista de retorno de manutenção |
| QuiPrv | Number(007,0) | Sim | Quilometragem do Veículo Prevista para Manutenção |
| ClaMan | Number(001,0) | Sim | Classificação da Manutenção |
| TipClb | Number(001,0) | Sim | Tipo de Colaborador Solicitante do Agendamento |
| EmpSol | Number(004,0) | Sim | Código da Empresa Solicitante da Manutenção |
| TclSol | Number(001,0) | Sim | Tipo de Colaborador Solicitante |
| CadSol | Number(009,0) | Sim | Cadastro do Autorizador Solicitante da Manutenção |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outra Unidade |
| ObsAgm | String(300) | Sim | Observação do Agendamento |
| AgmUti | String(001) | Sim | Indica que o Agendamento  foi Utilizado |
| CodSol | Number(006,0) | Sim | Código da Solicitação de Oficina |
| CodOem | Number(008,0) | Sim | Código da Empresa que Gerou o Orçamento |

---

## Chave Primária

- PlaVei
- DatAgm
- HorAgm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088AGN_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

