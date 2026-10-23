# R038HCE

## Descrição

Histórico de Colaboradores Cedidos

---

## Resumo

- Campos: 68
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo do colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatIni | Date | Não | Data de início da cessão |
| TipCes | Number(001,0) | Sim | Informar se a empresa de destino está no próprio sistema ou em outro sistema |
| EmpAtu | Number(004,0) | Sim | Código da empresa para qual o colaborador foi cedido |
| CadAtu | Number(009,0) | Sim | Código do novo cadastro na empresa de destino |
| FicReg | Number(009,0) | Sim | Número da ficha registro na empresa de destino |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
| CgcCes | Number(015,0) | Sim | Número da Inscrição (CNPJ/CPF) da empresa para o qual o colaborador foi cedido |
| CfjIns | String(014) | Sim | Número da Inscrição (CNPJ/CPF) da empresa para o qual o colaborador foi cedido |
| TipOnu | Number(001,0) | Sim | Ônus Cessão |
| SitAfa | Number(003,0) | Sim | Código da situação que o afastamento será gerado |
| DatTer | Date | Sim | Data de término da cessão |
| ObsHis | String(500) | Sim | Observação |
| CodTap | Number(003,0) | Sim | Código do tipo de atuação na empresa de destino |
| EstPos | Number(003,0) | Sim | Código da estrutura de posto de trabalho na empresa de destino |
| PosTra | String(024) | Sim | Código do posto de trabalho na empresa de destino |
| MotPos | Number(003,0) | Sim | Motivo de alteração do posto de trabalho |
| CodFil | Number(006,0) | Sim | Código da filial na empresa de destino |
| TabOrg | Number(004,0) | Sim | Código da tabela de organograma na empresa de destino |
| NumLoc | Number(009,0) | Sim | Local do organograma na empresa de destino |
| CodCcu | String(018) | Sim | Código do centro de custo na empresa de destino |
| NatDes | Number(003,0) | Sim | Código da natureza de despesa na empresa de destino |
| EstCar | Number(004,0) | Sim | Código da estrutura de cargos na empresa de destino |
| CodCar | String(024) | Sim | Código do cargo na empresa de destino |
| CarVag | String(024) | Sim | Código do novo cargo para ocupação da vaga |
| MotCar | Number(003,0) | Sim | Motivo da alteração de cargo |
| CodVin | Number(002,0) | Sim | Tipo de vínculo na empresa de destino |
| CodEsc | Number(009,0) | Sim | Código da escala na empresa de destino |
| CodTma | Number(001,0) | Sim | Código da turma da escala na empresa de destino |
| TurInt | Number(009,0) | Sim | Código da turma de intervalo na empresa de destino |
| HorBas | Number(004,0) | Sim | Horário Base (Segunda a Sexta-Feira) |
| HorSab | Number(004,0) | Sim | Horário de Sábado |
| HorSem | Number(010,0) | Sim | Horas Semanais |
| HorDsr | Number(010,0) | Sim | Horas de DSR |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ValSal | Number(013,4) | Sim | Valor do Salário |
| CplSal | Number(013,4) | Sim | Valor Complementar ao Salário |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| TipEst | Number(001,0) | Sim | Tipo de Estrutura |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerRea | Number(008,5) | Sim | Percentual de Reajuste |
| MotSal | Number(003,0) | Sim | Motivo da alteração salarial |
| CodSin | Number(004,0) | Sim | Código do Sindicato |
| SocSin | String(001) | Sim | Sócio do Sindicato |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| ConFin | Number(007,0) | Sim | Conta Financeira |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| MotOri | Number(003,0) | Sim | Motivo de alteração do posto de trabalho |
| TapOri | Number(003,0) | Sim | Tipo de atuação na empresa de origem |
| EstOri | Number(003,0) | Sim | Estrutura de postos de trabalho na empresa de origem |
| PosOri | String(024) | Sim | Posto de trabalho na empresa de origem |
| OrgOri | Number(004,0) | Sim | Tabela de organograma na empresa de origem |
| LocOri | Number(009,0) | Sim | Local do organograma na empresa de origem |
| VinOri | Number(002,0) | Sim | Vínculo na empresa de origem |
| TipAdm | Number(002,0) | Sim | Tipo de Admissão |
| SitHce | Number(001,0) | Sim | Situação do Histórico de Cessão |
| TipCad | Number(001,0) | Sim | Tipo Cessão |
| OnuSin | Number(001,0) | Sim | Ônus da Remuneração |
| EnvESo | Number(001,0) | Sim | Enviar ao eSocial |
| ResOnu | String(001) | Sim | Ressarcimento Ônus |
| ResRem | String(001) | Sim | Responsável Remuneração |
| CmpAu1 | String(001) | Sim | Campo Auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo Auxiliar 2 |
| CmpAu3 | Date | Sim | Campo Auxiliar 3 |
| CmpAu4 | String(255) | Sim | Campo Auxiliar 4 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
