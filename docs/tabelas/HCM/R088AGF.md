# R088AGF

## Descrição

Agendamentos do Veículo

---

## Resumo

- Campos: 26
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatAgf | Date | Não | Data de Saída do Veículo |
| HorAgf | Number(005,0) | Não | Hora Saída Veículo |
| MotUso | Number(003,0) | Sim | Motivo Uso do Veículo |
| EmpSol | Number(004,0) | Sim | Código da Empresa Solicitante do Agendamento |
| TClSol | Number(001,0) | Sim | Tipo de Colaborador Solicitante do Agendamento |
| CadSol | Number(009,0) | Sim | Cadastro Solicitante do Agendamento |
| DatRet | Date | Sim | Data Prevista para Retorno |
| HorRet | Number(005,0) | Sim | Hora Prevista para Retorno |
| DesVei | String(040) | Sim | Local de Destino do Veículo |
| QtdPas | Number(002,0) | Sim | Quantidade Permitida de Passageiros |
| QtdKgs | Number(009,3) | Sim | Quantidade de Kilogramas para Transportar |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TClAut | Number(001,0) | Sim | Tipo de Colaborador do Autorizador do Agendamento |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| EmpCon | Number(004,0) | Sim | Código da Empresa do Condutor |
| TClCon | Number(001,0) | Sim | Tipo de Colaborador Condutor |
| CadCon | Number(009,0) | Sim | Cadastro do Condutor |
| ObsAgf | String(080) | Sim | Observação do Agendamento |
| VeiUti | String(001) | Sim | Indica que o Veículo do Agendado foi Utilizado (Agendamento Executado) |
| StaAtu | Number(001,0) | Sim | Status do Histórico de Agendamento |
| SisAgm | Number(001,0) | Sim | Indica que Sistema é proprietário do Agendamento |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Efetuou o Agendamento |
| DatAtu | Date | Sim | Data que foi inserido/alterado o registro |
| HorAtu | Number(005,0) | Sim | Hora que foi inserido/alterado o registro |
| CodSol | Number(006,0) | Sim | Código da Solicitação de Uso de Veículo |

---

## Chave Primária

- PlaVei
- DatAgf
- HorAgf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088AGF_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

