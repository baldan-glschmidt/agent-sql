# R088AGP

## Descrição

Agendamento Passageiros do Veículo

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatAgf | Date | Não | Data de Saída do Veículo |
| HorAgf | Number(005,0) | Não | Hora Saída Veículo |
| SeqPas | Number(002,0) | Não | Sequência do Passageiro |
| TipPaV | Number(001,0) | Sim | Tipo do Passageiro do Veículo |
| NumEmp | Number(004,0) | Sim | Código da Empresa do Colaborador Passageiro |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador Passageiro |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Passageiro |
| CadOcr | Number(009,0) | Sim | Cadastro do Colaborador de Outra Unidade Passageiro |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante Passageiro |
| NumDoc | String(020) | Sim | Número do Documento do Visitante Passageiro |
| NomPas | String(040) | Sim | Nome do Visitante Passageiro |
| CodOem | Number(008,0) | Sim | Código da Empresa do Visitante Passageiro |
| NomOem | String(060) | Sim | Nome da Empresa do Visitante Passageiro |
| CodCcu | String(018) | Sim | Código Centro Custo Contábil |
| PerUti | Number(006,2) | Sim | Percentual de Utilização do Passageiro |

---

## Chave Primária

- PlaVei
- DatAgf
- HorAgf
- SeqPas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088AGP_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088AGP_002

**Tabela:** R088AGF

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |
| DatAgf | DatAgf |
| HorAgf | HorAgf |

