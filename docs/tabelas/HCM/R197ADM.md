# R197ADM

## Descrição

Cenário - Admissões Coletivas p/ Centro de Custo

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
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
| QtdAdm | Number(004,0) | Sim | Quantidade de colaboradores envolvidos |
| ObsAdm | String(250) | Sim | Observação sobre a admissão |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| ValSal | Number(013,4) | Sim | Salário |

---

## Chave Primária

- NumEmp
- CodCen
- CodCcu
- EstCar
- CodCar
- CmpQua

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R197ADM_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R197ADM_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R197ADM_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

