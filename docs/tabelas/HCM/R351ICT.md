# R351ICT

## Descrição

S-2500 - eSocial - Informações do contrato de trabalho

---

## Resumo

- Campos: 58
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| IdeSeq | Number(005,0) | Não | Sequência parcial |
| SeqPtb | Number(009,0) | Não | Sequência |
| SeqIct | Number(009,0) | Não | Sequência |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipCon | Number(001,0) | Sim | Tipo de contrato referente ao processo judicial ou a demanda submetida à CCP ou ao NINTER |
| IndCon | String(001) | Sim | Indicativo se possui informação no evento S-2190, S-2200 ou S-2300 no declarante |
| AdmOri | Date | Sim | Data de admissão original do vínculo (data de admissão antes da alteração) |
| IndRei | String(001) | Sim | Indicativo de reintegração do empregado |
| IndCat | String(001) | Sim | Houve reconhecimento de categoria do trabalhador diferente da cadastrada |
| IndNat | String(001) | Sim | Houve reconhecimento de natureza da atividade diferente da cadastrada |
| IndMot | String(001) | Sim | Houve reconhecimento de motivo desligamento diferente do informado |
| IndUni | String(001) | Sim | Houve reconhecimento de unicidade contratual |
| NumMat | String(030) | Sim | Matrícula atribuída ao trabalhador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| DatIni | Date | Sim | Data de início de TSVE |
| CodCbo | String(006) | Sim | Classificação Brasileira de Ocupações |
| NatAti | Number(001,0) | Sim | Código da natureza da atividade |
| RegTra | Number(001,0) | Sim | Tipo de regime trabalhista |
| RegPre | Number(001,0) | Sim | Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares) |
| DatAdm | Date | Sim | Data de admissão do trabalhador |
| TmpPar | Number(002,0) | Sim | Código relativo ao tipo de contrato em tempo parcial |
| ConTra | Number(001,0) | Sim | Tipo de contrato de trabalho |
| TerCon | Date | Sim | Data do término do contrato por prazo determinado |
| ClaAss | String(001) | Sim | Contém cláusula assecuratória do direito recíproco de rescisão antes da data de seu término |
| ObjDet | String(255) | Sim | Indicação do objeto determinante da contratação por prazo determinado |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do empregador anterior |
| NumIns | Number(014,0) | Sim | Número de inscrição do empregador anterior - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição do empregador anterior |
| MatAnt | String(030) | Sim | Matrícula do trabalhador no empregador anterior |
| DatTrf | Date | Sim | Data da transferêcia do empregado para o empregador declarante |
| DatDes | Date | Sim | Data de desligamento do vínculo (Último dia trabalhado) |
| MotDes | Number(002,0) | Sim | Código do motivo de desligamento |
| FimAPI | Date | Sim | Data projetada para o término do aviso prévio indenizado |
| DatTer | Date | Sim | Data de término de TSVE |
| MotTSV | Number(002,0) | Sim | Motivo do término do diretor não empregado, com FGTS |
| TpInRp | Number(001,0) | Sim | Tipo de inscrição do estabelecimento responsável pelo pagamento |
| NrInRp | Number(014,0) | Sim | Número de inscrição do estabelecimento responsável pelo pagamento - Obsoleto |
| CfjRes | String(014) | Sim | Número de inscrição do estabelecimento responsável pelo pagamento |
| CmpIni | Date | Sim | Competência inicial a que se refere o processo ou conciliação |
| CmpFim | Date | Sim | Competência final a que se refere o processo ou conciliação |
| RepPro | Number(001,0) | Sim | Repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER |
| VlrRem | Number(015,2) | Sim | Valor total das verbas remuneratórias a serem pagas ao trabalhador |
| VlrAPI | Number(015,2) | Sim | Valor do aviso prévio indenizado pago ao empregado |
| Vlr13A | Number(015,2) | Sim | Valor da projeção do aviso prévio indenizado sobre o 13º salário |
| VlrInd | Number(015,2) | Sim | Valor total das demais verbas indenizatórias a serem pagas ao trabalhador |
| VlrBas | Number(015,2) | Sim | Valor da base de cálculo para recolhimento da indenização compensatória (multa rescisória) do FGTS |
| IndCom | String(001) | Sim | A indenização compensatória (multa rescisória) do FGTS transacionada foi paga ao trabalhador |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do Colaborador |
| PenAli | Number(001,0) | Sim | Indicativo de pensão alimentícia |
| PerAli | Number(005,2) | Sim | Percentual destinado ao alimentando |
| VlrAli | Number(014,2) | Sim | Valor destinado ao alimentando |
| IndSSd | String(001) | Sim | Houve decisão para pagamento da indenização substitutiva do seguro-desemprego |
| IndSAs | String(001) | Sim | Houve decisão para pagamento da indenização substitutiva de abono salarial |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb
- SeqIct

---

## Índices

### R351ICTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
