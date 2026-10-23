# R088CVF

## Descrição

Geração e Apropriação de Custos por Veículos

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatCpt | Date | Não | Mês/Ano de Competência |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| PlaVei | String(010) | Não | Placa do Veículo |
| CodCcu | String(018) | Não | Código Centro de Custo Contábil |
| QuiPer | Number(008,2) | Sim | Quilometragem Total Percorrida na Movimentação |
| ValQui | Number(015,2) | Sim | Valor Total da Quilometragem do Veículo |
| ValDsp | Number(015,2) | Sim | Valor Despesa do Rateio por Centro de Custo e Veículo |
| SitReg | Number(001,0) | Sim | Situação do Registro |
| CusKrd | Number(011,2) | Sim | Valor do Custo por Km Rodado |
| ValCon | Number(015,2) | Sim | Valor do Contrato do Veículo |
| ValAba | Number(015,2) | Sim | Valor dos Abastecimentos do Veículo |
| ValInf | Number(015,2) | Sim | Valor das Infrações do Veículo |
| ValMan | Number(015,2) | Sim | Valor das Manutenções do Veículo |
| ValLic | Number(015,2) | Sim | Valor dos Impostos do Veículo |
| ValSeg | Number(015,2) | Sim | Valor do Seguro do Veículo |
| ValSin | Number(015,2) | Sim | Valor dos Sinistros do Veículo |

---

## Chave Primária

- DatCpt
- NumEmp
- PlaVei
- CodCcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088CVF_001

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R088CVF_002

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

### IR_R088CVF_003

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

