# R088VCS

## Descrição

Saída de Carga e Descarga de Veículos

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
| DatChg | Date | Não | Data de Chegada do Veículo |
| HorChg | Number(005,0) | Não | Hora de Chegada do Veículo |
| DatSai | Date | Sim | Data de Saída do Veículo |
| HorSai | Number(005,0) | Sim | Hora de Saída Veículo |
| PorSai | Number(003,0) | Sim | Código da Portaria |
| PesSai | Number(009,3) | Sim | Peso Bruto Saída da Carga e Veículo |
| PesLiq | Number(009,3) | Sim | Peso Líquido da Carga |
| PesNfs | Number(009,3) | Sim | Peso Destacado na Nota Fiscal |
| TmpPer | Number(010,0) | Sim | Tempo de Permanência do Veículo na Movimentação |
| EmpSai | Number(004,0) | Sim | Código da Empresa do Colaborador no Cadastro da Saída |
| TipSai | Number(001,0) | Sim | Tipo de Colaborador no Cadastro da Saída |
| CadSai | Number(009,0) | Sim | Cadastro do Colaborador no Cadastro de Saída |
| EmpRsd | Number(004,0) | Sim | Código da Empresa do Responsável pelo Cadastro da Saída |
| TipRsd | Number(001,0) | Sim | Tipo de Colaborador Responsável pelo Cadastro da Saída |
| CadRsd | Number(009,0) | Sim | Cadastro do Responsável pelo Cadastro de Saída |
| NumSen | Number(009,0) | Sim | Número da Senha de Chegada |
| ObsSai | String(080) | Sim | Observação da Movimentação de Carga e Descarga |
| EmpRps | Number(004,0) | Sim | Código da Empresa do Responsável pelo Cadastro da Pesagem |
| TipRps | Number(001,0) | Sim | Tipo de Colaborador Responsável pelo Cadastro da Pesagem |
| CadRps | Number(009,0) | Sim | Cadastro do Responsável pelo Cadastro de Pesagem |
| DatRps | Date | Sim | Data de Pesagem do Veículo |
| HorRps | Number(005,0) | Sim | Hora de Pesagem Veículo |
| StaPes | Number(001,0) | Sim | Status da Pesagem na Saída de Carga e Descarga |
| PesSa2 | Number(009,3) | Sim | Peso Bruto Saída da Carga e Veículo 2 |
| PesSa3 | Number(009,3) | Sim | Peso Bruto Saída da Carga e Veículo 3 |

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

### IR_R088VCS_000

**Tabela:** R088VEI

| Origem | Destino |
|--------|---------|
| PlaVei | PlaVei |

