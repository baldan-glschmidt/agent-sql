# R088MVS

## Descrição

Movimento de Veículos Prestadores Serviço

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PlaVei | String(010) | Não | Placa do Veículo |
| DatEnt | Date | Não | Data de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| CodOem | Number(008,0) | Sim | Código da Outra Empresa (Terceiro/Parceiro) |
| MotMvs | Number(001,0) | Sim | Motivo da Entrada do Veículo |
| EmpRes | Number(004,0) | Sim | Código da Empresa Responsável pela Entrada |
| TclRes | Number(001,0) | Sim | Tipo de Colaborador Responsável pela Entrada |
| CadRes | Number(009,0) | Sim | Cadastro do Autorizador Responsável pela Entrada |
| ObsMov | String(080) | Sim | Observação do Movimento |
| DatSai | Date | Sim | Data da Saída da Empresa |
| HorSai | Number(005,0) | Sim | Hora da Saída da Empresa |
| PorEnt | Number(003,0) | Sim | Código da Portaria da Entrada |
| PorSai | Number(003,0) | Sim | Código da Portaria da Saída |
| NumEmp | Number(004,0) | Sim | Código da empresa |
| TipCol | Number(001,0) | Sim | Tipo colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do colaborador |

---

## Chave Primária

- PlaVei
- DatEnt
- HorEnt

---

## Índices

### R088MVSIndice2

**Tipo:** Não unico

Campos:
- PlaVei

---

## Relacionamentos

Nenhum relacionamento cadastrado.
