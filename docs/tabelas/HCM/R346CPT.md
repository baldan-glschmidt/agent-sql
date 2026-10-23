# R346CPT

## Descrição

eSocial JR - Processo Trabalhista

---

## Resumo

- Campos: 75
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodPro | Number(009,0) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| TipRes | Number(001,0) | Sim | Tipo de inscrição do contribuinte (responsável direto) |
| InsRes | Number(014,0) | Sim | Número de inscrição do contribuinte (responsável direto) - Obsoleto |
| CfjRes | String(014) | Sim | Número de inscrição do contribuinte (responsável direto) |
| OriPro | Number(001,0) | Sim | Origem do processo/demanda |
| ObsPro | String(999) | Sim | Observações relacionadas ao processo judicial ou à demanda submetida à CCP ou ao NINTER |
| DatSen | Date | Sim | Data da sentença ou da homologação do acordo do processo judicial |
| UfVara | String(002) | Sim | Unidade da Federação onde está localizada a Vara em que o processo tramitou |
| CodMun | Number(007,0) | Sim | Código do município, conforme tabela do IBGE |
| IdeVar | String(004) | Sim | Código de identificação da Vara em que o processo tramitou |
| DatCon | Date | Sim | Data da conciliação |
| CelAco | Number(001,0) | Sim | Âmbito de celebração do acordo |
| CnpjSi | Number(014,0) | Sim | CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NomTra | String(070) | Sim | Nome do trabalhador |
| DatNas | Date | Sim | Data de nascimento do trabalhador |
| TipCon | Number(001,0) | Sim | Tipo de contrato a que se refere o processo judicial ou a demanda submetida à CCP ou ao NINTER |
| IndCon | String(001) | Sim | Contrato possui informação no evento S-2190, S-2200 ou S-2300 no declarante |
| DatOri | Date | Sim | Data de admissão original do vínculo (data de admissão antes da alteração) |
| DatTSV | Date | Sim | Data de início de TSVE |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| NumMat | String(030) | Sim | Matrícula atribuída ao trabalhador |
| IndRet | String(001) | Sim | Indicativo de reintegração do empregado |
| IndCat | String(001) | Sim | Houve reconhecimento de categoria do trabalhador diferente da cadastrada pelo declarante |
| IndNat | String(001) | Sim | Houve reconhecimento de natureza da atividade diferente da cadastrada pelo declarante |
| IndMot | String(001) | Sim | Houve reconhecimento de motivo de desligamento diferente da cadastrada pelo declarante |
| IndUni | String(001) | Sim | Houve reconhecimento de unicidade contratual |
| CodCbo | String(006) | Sim | Código CBO - Classificação Brasileira de Ocupações |
| NatAti | Number(001,0) | Sim | Código da natureza da atividade |
| RegTra | Number(001,0) | Sim | Tipo de regime trabalhista |
| RegPre | Number(001,0) | Sim | Tipo de regime previdenciário (ou Sistema de Proteção Social dos Militares) |
| DatAdm | Date | Sim | Data de admissão do trabalhador |
| TmpPar | Number(002,0) | Sim | Código relativo ao tipo de contrato em tempo parcial |
| ConTra | Number(001,0) | Sim | Tipo de contrato de trabalho |
| TerCon | Date | Sim | Data do término do contrato por prazo determinado |
| ClaAss | String(001) | Sim | Cláusula assecuratória do direito recíproco de rescisão antes da data de seu término |
| ObjDet | String(255) | Sim | Objeto determinante da contratação por prazo determinado (obra, serviço, safra, etc.) |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do empregador anterior |
| NumIns | Number(014,0) | Sim | Número de inscrição do empregador anterior - Obsoleto |
| CfjAnt | String(014) | Sim | Número de inscrição do empregador anterior |
| MatAnt | String(030) | Sim | Matrícula do trabalhador no empregador anterior |
| DatTrf | Date | Sim | Data da transferêcia do empregado para o empregador declarante |
| DatDes | Date | Sim | Data de desligamento do vínculo (último dia trabalhado) |
| MotDes | Number(002,0) | Sim | Código do motivo de desligamento |
| FimAPI | Date | Sim | Data projetada para o término do aviso prévio indenizado |
| DatTer | Date | Sim | Data de término de TSVE |
| MotTSV | Number(002,0) | Sim | Motivo do término do diretor não empregado, com FGTS |
| TpInRp | Number(001,0) | Sim | Tipo de inscrição do estabelecimento responsável pelo pagamento |
| NrInRp | Number(014,0) | Sim | Número de inscrição do estabelecimento responsável pelo pagamento - Obsoleto |
| CfjEst | String(014) | Sim | Número de inscrição do estabelecimento responsável pelo pagamento |
| CmpIni | Date | Sim | Competência inicial a que se refere o processo ou conciliação |
| CmpFim | Date | Sim | Competência final a que se refere o processo ou conciliação |
| RepPro | Number(001,0) | Sim | Repercussão do processo trabalhista ou de demanda submetida à CCP ou ao NINTER |
| VlrRem | Number(015,2) | Sim | Valor total das verbas remuneratórias a serem pagas ao trabalhador |
| VlrAPI | Number(015,2) | Sim | Valor do aviso prévio indenizado pago ao empregado |
| Vlr13A | Number(015,2) | Sim | Valor da projeção do aviso prévio indenizado sobre o 13º salário |
| VlrInd | Number(015,2) | Sim | Valor total das demais verbas indenizatórias a serem pagas ao trabalhador |
| VlrBas | Number(015,2) | Sim | Valor da base de cálculo para recolhimento da indenização compensatória (multa rescisória) do FGTS |
| VlrJur | Number(015,2) | Sim | Valor total dos juros de mora |
| VlrCor | Number(015,2) | Sim | Valor total da correção monetária |
| IndCom | String(001) | Sim | A indenização compensatória (multa rescisória) do FGTS transacionada foi paga ao trabalhador |
| PenAli | Number(001,0) | Sim | Indicativo de pensão alimentícia para fins de retenção de FGTS |
| PerAli | Number(005,2) | Sim | Percentual a ser destinado a pensão alimentícia |
| VlrAli | Number(014,2) | Sim | Valor da pensão alimentícia |
| IndSSd | String(001) | Sim | Houve decisão para pagamento da indenização substitutiva do seguro-desemprego |
| IndSAs | String(001) | Sim | Houve decisão para pagamento da indenização substitutiva de abono salarial |
| OriInf | Number(001,0) | Sim | Origem das informações dos dados |
| CodAca | Number(007,0) | Sim | Código da Ação gerada pelo cadastro de Ações |
| AdmRes | Date | Sim | Data de admissão do trabalhador no estabelecimento responsável pelo pagamento |
| MatRes | String(030) | Sim | Matrícula atribuída ao trabalhador no estabelecimento responsável pelo pagamento |
| VlrPat | Number(014,2) | Sim | Valor total da cota patronal incidente sobre a remuneração paga ao trabalhador, que será objeto de requisição autônoma |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPro

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
