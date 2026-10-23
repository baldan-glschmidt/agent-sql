# R088PTX

## Descrição

Passageiros na Movimentação de Táxis

---

## Resumo

- Campos: 31
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatSol | Date | Não | Data da Movimentação do Veículo |
| HorSol | Number(005,0) | Não | Hora da Movimentação do Veículo |
| SeqSol | Number(002,0) | Não | Sequência da Movimentação |
| SeqPas | Number(002,0) | Não | Sequência do Passageiro |
| CodTax | Number(004,0) | Sim | Código Taxista |
| PlaVei | String(010) | Sim | Placa do Veículo |
| DatSai | Date | Sim | Data de Saída do Veículo |
| HorSai | Number(005,0) | Sim | Hora Saída do Veículo |
| CodPlt | Number(005,0) | Sim | Código do Site |
| CodIti | Number(004,0) | Sim | Código do Itinerário |
| TipPes | Number(001,0) | Sim | Tipo da pessoa passageira da movimentação |
| EmpSol | Number(004,0) | Sim | Código da Empresa do Solicitente da Movimentação |
| TipSol | Number(001,0) | Sim | Tipo do Solicitante da Movimentação |
| CadSol | Number(009,0) | Sim | Cadastro do Solicitante da Movimentação |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |
| EmpAut | Number(004,0) | Sim | Código da Empresa do Autorizador do Agendamento |
| TipAut | Number(001,0) | Sim | Tipo Autorizador da Movimentação |
| CadAut | Number(009,0) | Sim | Cadastro do Autorizador do Agendamento |
| IndTra | Number(001,0) | Sim | Indicação do Trajeto da Movimentação |
| CodCcu | String(018) | Sim | Código Centro de Custo Contábil |
| ValIti | Number(011,2) | Sim | Valor do Itinerário da Movimentação de Táxi |
| ObsPas | String(080) | Sim | Observação do Passageiro |
| ValRat | Number(011,2) | Sim | Valor do Rateio da Movimentação de Táxi por Passageiro |
| CodOmi | Number(009,0) | Sim | Informar Conta para Apropriar Custo (Investimento, Manutenção etc) |
| DatFim | Date | Sim | Data Final da Viagem |
| HorFim | Number(005,0) | Sim | Hora Final da Viagem |
| EmpOcr | Number(004,0) | Sim | Empresa do Colaborador de Outras Unidades Passageiro da Movimentação |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outras Unidades Passageiro da Movimentação |

---

## Chave Primária

- NumEmp
- CodFil
- DatSol
- HorSol
- SeqSol
- SeqPas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088PTX_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R088PTX_004

**Tabela:** R088MTX

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| DatSol | DatSol |
| HorSol | HorSol |
| SeqSol | SeqSol |

