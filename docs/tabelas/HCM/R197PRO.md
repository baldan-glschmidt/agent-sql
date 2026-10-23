# R197PRO

## Descrição

Cenário - Promoções Coletivas p/ Centro de Custo

---

## Resumo

- Campos: 15
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
| SeqPro | Number(003,0) | Não | Sequência dos registros de promoções |
| CarDes | String(024) | Sim | Código do cargo de destino |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| ValSal | Number(013,4) | Sim | Salário proposto para a promoção |
| QtdPro | Number(004,0) | Sim | Quantidade de colaboradores envolvidos |
| ObsPro | String(250) | Sim | Observação sobre a promoção |
| ProInd | String(001) | Sim | Indica se a promoção é individual |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| CodMot | Number(003,0) | Sim | Motivo da alteração de cargo ou salário nas promoções coletivas |

---

## Chave Primária

- NumEmp
- CodCen
- CodCcu
- EstCar
- CodCar
- CmpQua
- SeqPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R197PRO_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R197PRO_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R197PRO_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

