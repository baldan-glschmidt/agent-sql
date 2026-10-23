# R088VCE

## Descrição

Entrada de Carga e Descarga de Veículos

---

## Resumo

- Campos: 25
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatChg | Date | Não | Data de Chegada do Veículo |
| HorChg | Number(005,0) | Não | Hora de Chegada do Veículo |
| DatEnt | Date | Sim | Data de Entrada do Veículo |
| HorEnt | Number(005,0) | Sim | Hora de Entrada Veículo |
| PorEnt | Number(003,0) | Sim | Código da Portaria da Entrada |
| PesEnt | Number(009,3) | Sim | Peso Bruto Entrada da Carga e Veículo |
| NotFis | String(050) | Sim | Notas Fiscais de Movimentação |
| EmpEnt | Number(004,0) | Sim | Código da Empresa do Colaborador do Cadastro da Entrada |
| TipEnt | Number(001,0) | Sim | Tipo de Colaborador do Cadastro da Entrada |
| CadEnt | Number(009,0) | Sim | Cadastro do Colaborador do Cadastro de Entrada |
| EmpRnt | Number(004,0) | Sim | Código da Empresa do Responsável pelo Cadastro da Entrada |
| TipRnt | Number(001,0) | Sim | Tipo de Colaborador Responsável pelo Cadastro da Entrada |
| CadRnt | Number(009,0) | Sim | Cadastro do Responsável pelo Cadastro de Entrada |
| ObsEnt | String(080) | Sim | Observação de Entrada da Movimentação de Carga e Descarga |
| NumSen | Number(009,0) | Sim | Número da Senha de Chegada |
| NumCra | Number(012,0) | Sim | Código do Crachá |
| EmpRpe | Number(004,0) | Sim | Código da Empresa do Responsável pela pesagem da Entrada |
| TipRpe | Number(001,0) | Sim | Tipo de Colaborador Responsável pelo Cadastro da Pesagem |
| CadRpe | Number(009,0) | Sim | Cadastro do Colaborador do Responsável pela Pesagem |
| DatRpe | Date | Sim | Data de Pesagem Entrada do Veículo |
| HorRpe | Number(005,0) | Sim | Hora do Pesagem Entrada Veículo |
| CraVei | Number(012,0) | Sim | Crachá Veículo |
| PesEn2 | Number(009,3) | Sim | Peso Bruto Entrada da Carga e Veículo 2 |
| PesEn3 | Number(009,3) | Sim | Peso Bruto Entrada da Carga e Veículo 3 |

---

## Chave Primária

- PlaVei
- DatChg
- HorChg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R088VCE_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

