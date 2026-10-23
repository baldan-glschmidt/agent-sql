# R038HFI

## Descrição

Histórico Filial

---

## Resumo

- Campos: 49
- Chave Primária: 4 campo(s)
- Índices: 4
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração da Filial |
| EmpAtu | Number(004,0) | Sim | Código da Nova Empresa |
| CodTap | Number(003,0) | Sim | Define qual Tipo de atuação o Colaborador exercerá no seu Posto |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Código do Posto de Trabalho em que o Colaborador atuará |
| CodFil | Number(006,0) | Sim | Código da Nova Filial |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma da Nova Empresa |
| NumLoc | Number(009,0) | Sim | Local do Organograma da Nova Empresa |
| CadAtu | Number(009,0) | Sim | Código do Novo Cadastro |
| CodCcu | String(018) | Sim | Código do Novo Centro de Custo |
| NatDes | Number(003,0) | Sim | Nova Natureza de Despesa do C.Custo |
| TipAdm | Number(002,0) | Sim | Tipo de Admissão |
| FicReg | Number(009,0) | Sim | Número da Ficha Registro |
| ConTov | String(001) | Sim | Considerar Admissão p/ Cálculo do Turn-Over |
| StaAcc | Number(001,0) | Sim | Status da Atualização na Tabela CONTROLE (Acesso On-Line) |
| MotPos | Number(003,0) | Sim | Motivo de alteração do Posto de Trabalho |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Novo Cargo |
| CodMot | Number(003,0) | Sim | Motivo da Alteração do Cargo |
| CodEsc | Number(009,0) | Sim | Código da Nova Escala |
| CodTma | Number(001,0) | Sim | Código da Nova Turma da Escala |
| TurInt | Number(009,0) | Sim | Código da Turma de Intervalo |
| HorBas | Number(004,0) | Sim | Horário Base (Segunda a Sexta-Feira) |
| HorSab | Number(004,0) | Sim | Horário de Sábado |
| HorSem | Number(010,0) | Sim | Horas Semanais |
| HorDsr | Number(010,0) | Sim | Horas de DSR |
| CodMts | Number(003,0) | Sim | Motivo da Alteração Salarial |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ValSal | Number(013,4) | Sim | Salário Atual |
| CplSal | Number(013,4) | Sim | Valor Complementar ao Salário |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| TipEst | Number(001,0) | Sim | Tipo de Estrutura |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerDes | Number(005,2) | Sim | Percentual Desempenho |
| PerRea | Number(008,5) | Sim | % de Reajuste Concedido |
| CodSin | Number(004,0) | Sim | Código do Sindicato |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| ConFin | Number(007,0) | Sim | Conta Financeira |
| CodVin | Number(002,0) | Sim | Tipo de Vínculo |
| CarVag | String(024) | Sim | Código do novo cargo para ocupação da vaga |
| SocSin | String(001) | Sim | Sócio do Sindicato |
| AdmEso | Number(001,0) | Sim | Tipo de admissão do trabalhador |
| TraBHr | Number(001,0) | Sim | Tratar banco de horas |
| CodBHr | Number(005,0) | Sim | Banco de horas destino |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

### R038HFIIndice2

**Tipo:** Não unico

Campos:
- StaHis
- DatAlt

### R038HFIIndice3

**Tipo:** Não unico

Campos:
- EmpAtu
- CodFil

### R038HFIIndice4

**Tipo:** Não unico

Campos:
- CadAtu
- DatAlt

### R038HFIIndice5

**Tipo:** Não unico

Campos:
- TipCol
- NumEmp
- NumCad
- EmpAtu
- CadAtu
- DatAlt

---

## Relacionamentos

### IR_R038HFI_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R038HFI_008

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| EmpAtu | NumEmp |
| CodFil | CodFil |

