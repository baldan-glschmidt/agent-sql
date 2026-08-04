# E210EST

## Descrição

Estoques - Produtos por Depósito

---

## Resumo

- Campos: 53
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto em estoque |
| CodDer | String(007) | Não | Código da derivação do produto em estoque |
| CodDep | String(010) | Não | Código do depósito |
| DatIni | Date | Sim | Data do saldo inicial do produto em estoque |
| SalIni | Number(014,5) | Sim | Saldo inicial do produto em estoque no depósito |
| MskDep | String(018) | Sim | Máscara do depósito |
| NivDep | Number(001,0) | Sim | Nível do depósito conforme a máscara |
| UniMed | String(003) | Não | Unidade de medida de controle do estoque do produto |
| EstNeg | String(001) | Não | Indicativo se aceita ou não estoque negativo |
| QtdEst | Number(014,5) | Sim | Quantidade física total do estoque no depósito |
| QtdBlo | Number(014,5) | Sim | Quantidade de estoque bloqueado manualmente |
| QtdRes | Number(014,5) | Sim | Quantidade do estoque reservado (empenho) |
| QtdRae | Number(014,5) | Sim | Quantidade de reserva exclusiva do estoque |
| QtdOrd | Number(014,5) | Sim | Quantidade pendente em ordens de produção ou compra |
| QtdCcl | Number(014,5) | Sim | Quantidade consignada para clientes |
| QtdCfo | Number(014,5) | Sim | Quantidade consignada de fornecedores |
| EstRep | Number(014,5) | Sim | Quantidade de estoque para reposição - ponto de reposição |
| EstMin | Number(014,5) | Sim | Quantidade  mínima em estoque para análise de reposição |
| EstMax | Number(014,5) | Sim | Quantidade máxima em estoque para análise de reposição |
| EstMid | Number(004,0) | Sim | Quantidade mínima em dias para análise de reposição |
| EstMad | Number(004,0) | Sim | Quantidade máxima em dias para análise de reposição |
| DatCcr | Date | Sim | Data inicial do consumo para cálculo do consumo por dia |
| DatCfr | Date | Sim | Data final do consumo para cálculo do consumo por dia |
| QtdCcr | Number(014,5) | Sim | Quantidade de consumo médio por dia no período |
| DatUen | Date | Sim | Data da última movimentação de entrada do produto no estoque |
| DatUsa | Date | Sim | Data da última movimentação de saída do produto no estoque |
| DatVal | Date | Sim | Data de validade do produto no depósito |
| IndInv | Number(001,0) | Sim | Indicativo se o item está em inventário com ou sem permissão de movimentação |
| SitEst | String(001) | Não | Situação do produto no depósito |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do estoque |
| ObsMot | String(250) | Sim | Observação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| PrzRsu | Number(004,0) | Sim | Prazo médio de ressuprimento do produto em dias |
| QtdEmb | Number(014,5) | Sim | Quantidade em embalagens de estocagem do produto |
| EstCap | Number(014,5) | Sim | Capacidade máxima de estocagem do produto |
| DatUan | Date | Sim | Data da Última Análise de Reposição |
| DisXpl | String(001) | Sim | Considera produtos deste depósito p/ o cálculo de necessidades |
| CodEnd | String(020) | Sim | Código do endereçamento do produto no depósito |
| LigEsp | String(001) | Sim | Indicativo se a ligação produto por depósito é considerada especial (análise de reposição para depósito filiais) |
| CurAbc | String(001) | Sim | Curva ABC (informar A, B ou C) através da classificação pela curva de quantidades em estoque |
| DdgUen | Date | Sim | Data de digitação da última movimentação de entrada do produto no estoque |
| HdgUen | Number(005,0) | Sim | Hora de digitação da última movimentação de entrada do produto no estoque |
| DdgUsa | Date | Sim | Data de digitação da última movimentação de saída do produto no estoque |
| HdgUsa | Number(005,0) | Sim | Hora de digitação da última movimentação de saída do produto no estoque |
| IndEma | String(001) | Sim | Participa da análise de evolução de estoque mínimo automatizado |
| USU_minest | Number(014,5) | Sim | Qantidade Minima de Estoque |
| USU_maxest | Number(014,5) | Sim | Quantidade Maxima de Estoque |
| USU_PtoCri | Number(014,5) | Sim | Ponto Crítico (nível baixo de estoque) |
| USU_PolCdi | String(001) | Sim | Está na Politica do CD |
| USU_USUEMB | String(001) | Sim | Usado para gerar MIN/MAX da embalagem? |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodDep

---

## Índices

### E210ESTIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodDep

---

## Relacionamentos

### IR_E210EST_002

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E210EST_003

**Tabela:** E205DEP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodDep | CodDep |

