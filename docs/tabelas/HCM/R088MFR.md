# R088MFR

## Descrição

Movimento da Frota

---

## Resumo

- Campos: 33
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatSai | Date | Não | Data de Saída do Veículo |
| HorSai | Number(005,0) | Não | Hora Saída Veículo |
| EmpCon | Number(004,0) | Sim | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Sim | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Sim | Cadastro do Condutor |
| PorSai | Number(003,0) | Sim | Código da Portaria de Saída do Veículo |
| MotUso | Number(003,0) | Sim | Motivo Uso do Veículo |
| DesVei | String(040) | Sim | Local de Destino do Veículo |
| QuiSai | Number(007,0) | Sim | Quilometragem do Veículo na Saída Portaria |
| QuiRet | Number(007,0) | Sim | Quilometragem do Veículo no Retorno |
| DatPrv | Date | Sim | Data Prevista para Retorno |
| HorPrv | Number(005,0) | Sim | Hora Prevista para Retorno |
| DatRet | Date | Sim | Data de Retorno do Veículo |
| HorRet | Number(005,0) | Sim | Hora do Retorno Veículo |
| PorRet | Number(003,0) | Sim | Código da Portaria de Retorno do Veículo |
| ObsMov | String(080) | Sim | Observação da Saída do Veículo |
| QtdPas | Number(002,0) | Sim | Quantidade de Passageiros |
| QtdKgs | Number(009,3) | Sim | Capacidade de carga para transporte (litros) |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador do Agendamento |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| EmpVSa | Number(004,0) | Sim | Código da Empresa do Vigilante da Saída |
| TclVSa | Number(001,0) | Sim | Tipo de Colaborador do Vigilante da Saída |
| CadVsa | Number(009,0) | Sim | Cadastro do Vigilante da Saída |
| EmpVRe | Number(004,0) | Sim | Código da Empresa do Vigilante do Retorno |
| TclVRe | Number(001,0) | Sim | Tipo de Colaborador do Vigilante do Retorno |
| CadVRe | Number(009,0) | Sim | Cadastro do Vigilante do Retorno |
| ComSai | Number(001,0) | Sim | Combustível Saída |
| ComRet | Number(001,0) | Sim | Combustível Retorno |
| DatAgf | Date | Sim | Data do Agendamento |
| HorAgf | Number(005,0) | Sim | Hora do Agendamento |
| CodSol | Number(006,0) | Sim | Código da Solicitação de Uso de Veículo |

---

## Chave Primária

- PlaVei
- DatSai
- HorSai

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088MFR_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

