# R197TRF

## Descrição

Cenário - Transferências Coletivas p/ Centro de Custo

---

## Resumo

- Campos: 21
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpQua | Date | Não | Data do Quadro |
| SeqTrf | Number(003,0) | Não | Sequência dos registros de transferências |
| EmpDes | Number(004,0) | Sim | Código da empresa de destino |
| CenDes | Number(004,0) | Sim | Código do cenário de destino |
| CodFil | Number(006,0) | Sim | Código da filial de destino |
| CcuDes | String(018) | Sim | Código do Centro de Custo de Destino |
| EstDes | Number(004,0) | Sim | Código da estrutura de cargos de destino |
| CarDes | String(024) | Sim | Código do cargo de destino |
| QtdTrf | Number(004,0) | Sim | Quantidade de colaboradores envolvidos |
| CmpTer | Date | Sim | Data de término da transferência |
| ObsTrf | String(250) | Sim | Observação sobre a transferência |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| DefOnu | String(001) | Sim | Define se a transferência de empresa terá ônus |
| CodMot | Number(003,0) | Sim | Motivo da alteração de cargo ou salário nas transferências coletivas |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| SalTrf | Number(013,4) | Sim | Salário de destino da Transferência |

---

## Chave Primária

- NumEmp
- CodCen
- CodCcu
- EstCar
- CodCar
- CmpQua
- SeqTrf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R197TRF_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R197TRF_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R197TRF_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

