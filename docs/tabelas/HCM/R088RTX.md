# R088RTX

## Descrição

Reserva de Táxis

---

## Resumo

- Campos: 29
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatRsv | Date | Não | Data da Reserva do Veículo |
| HorRsv | Number(005,0) | Não | Hora da Reserva do Veículo |
| SeqRsv | Number(002,0) | Não | Sequência da Reserva |
| SeqPas | Number(002,0) | Não | Sequência do Passageiro |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodIti | Number(004,0) | Sim | Código do Itinerário |
| TipPes | Number(001,0) | Sim | Tipo da pessoa passageira da movimentação |
| EmpSol | Number(004,0) | Sim | Código da Empresa do Solicitante da Movimentação |
| TipSol | Number(001,0) | Sim | Tipo Solicitante da Movimentação |
| CadSol | Number(009,0) | Sim | Cadastro do Solicitante da Movimentação |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TipAut | Number(001,0) | Sim | Tipo Autorizador da Movimentação |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| IndTra | Number(001,0) | Sim | Indicação do Trajeto da Movimentação |
| CodCcu | String(018) | Sim | Código Centro de Custo Contábil |
| ValIti | Number(012,3) | Sim | Valor do Itinerário da Movimentação de Táxi |
| CodOmi | Number(009,0) | Sim | Informar Conta para Apropriar Custo (Investimento, Manutenção etc) |
| DatIni | Date | Sim | Data Inicial da Viagem |
| HorIni | Number(005,0) | Sim | Hora Inicial da Viagem |
| DatFim | Date | Sim | Data Final da Viagem |
| HorFim | Number(005,0) | Sim | Hora Final da Viagem |
| RsvAge | String(001) | Sim | Reserva Agendada |
| ObsRtx | String(080) | Sim | Observação da Reserva |
| CodRot | Number(008,0) | Sim | Código da Roteirização de Táxis. |
| SolPen | String(001) | Sim | Solicitação Pendente |

---

## Chave Primária

- NumEmp
- CodFil
- DatRsv
- HorRsv
- SeqRsv
- SeqPas

---

## Índices

### R088RTXIndice2

**Tipo:** Não unico

Campos:
- CodRot

---

## Relacionamentos

### IR_R088RTX_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

