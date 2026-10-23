# R098REV

## Descrição

Revisões Equipamentos

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| TipSvc | Number(003,0) | Não | Código Tipo de Serviço |
| DatRev | Date | Não | Data da Revisão |
| SitRev | Number(001,0) | Sim | Situação da Revisão |
| EmpRev | Number(004,0) | Sim | Código da Empresa do Colaborador Responsável |
| TipCol | Number(001,0) | Sim | Tipo do Colaborador Responsável |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador Responsável |
| CodFab | Number(008,0) | Sim | Fabricante em que foi encaminhado o equipamento |
| DatSai | Date | Sim | Data da Saída do Equipamento |
| DatRet | Date | Sim | Data Retorno do Equipamento |
| STpEqp | Number(003,0) | Sim | Tipo do Equipamento Substituto |
| SCdEqp | Number(006,0) | Sim | Código do Equipamento |
| SCdLcz | Number(004,0) | Sim | Código da Localização do Substituído |
| ObsRev | String(250) | Sim | Observações |
| ValRev | Number(011,2) | Sim | Valor da revisão |
| NomArq | String(250) | Sim | Arquivo |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp
- TipSvc
- DatRev

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098REV_002

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

### IR_R098REV_003

**Tabela:** R098SVC

| Origem | Destino |
|--------|---------|
| TipSvc | TipSvc |

