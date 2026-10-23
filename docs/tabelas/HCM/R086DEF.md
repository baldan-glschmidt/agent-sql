# R086DEF

## Descrição

Definições do Segurança

---

## Resumo

- Campos: 121
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| ModCat | String(011) | Sim | Modelo do Gerador Relatórios Default para CAT |
| ConCat | String(001) | Sim | Permite registrar histórico de CAT |
| EntEpi | String(001) | Sim | Indica se permite entregar EPI sem instrução uso |
| InfExa | String(001) | Sim | Permite Informar Exame no Cadastro do PPRA |
| InfFun | String(001) | Sim | Permite Informar Funcionário no cadastro do PPRA |
| RquCur | String(001) | Sim | Considera requisito curso p/perfil profissiográfico previdenciário |
| ResExa | Number(001,0) | Sim | Define se apresenta exame, aso ou justificativa no  PPP |
| JusExa | String(200) | Sim | Justificativa para não informar exames no PPP |
| IndCri | String(001) | Sim | Critica inclusão de membro da brigada(Turno/Local) |
| ModEPI | String(011) | Sim | Modelo Relatório para protocolo de entrega de EPI |
| RquIda | String(001) | Sim | Imprime requisito idade no PPP |
| RquAlt | String(001) | Sim | Imprime requisito altura no PPP |
| RquPes | String(001) | Sim | Imprime requisito peso no PPP |
| RquSex | String(001) | Sim | Imprime requisito sexo  no PPP |
| RquIns | String(001) | Sim | Imprime requisito instrução no PPP |
| EmiEpi | String(001) | Sim | Imprime  EPI/EPC no PPP |
| AgtNoc | String(200) | Sim | Explanação sobre agente nocivo para impressão no PPP |
| ExpAgt | String(001) | Sim | Perigo/Fator de Risco a considerar no PPP - campo 27 |
| AprAgt | String(001) | Sim | Forma de apresentar a "exposição a agente nocivo" no PPP |
| EmiLim | String(001) | Sim | Imprime limite de tolerância no PPP |
| EmiDos | String(001) | Sim | Imprime dose no PPP |
| JusAss | String(200) | Sim | Justificativa para uso de assinatura eletrônica no PPP |
| DatCat | Date | Sim | Data referência p/considerar as CAT´s no PPP |
| JusCat | String(200) | Sim | Justificativa para constar no campo CAT do  PPP |
| EmiAgt | String(001) | Sim | Perigos/Fatores de Risco a serem considerados no PPP (campo 19) e eSocial |
| DatExa | Date | Sim | Data referência p/considerar os exames no PPP |
| ExaAdm | Number(003,0) | Sim | Tempo a considerar de exames antes admissão(em dias) |
| AprExa | Number(001,0) | Sim | Define forma de apresentar a identificação dos exames no PPP |
| ParExa | String(001) | Sim | Imprime o parecer ou os termos normal/alterado no PPP |
| DesRod | String(140) | Sim | Descrição p/constar no rodapé do PPP |
| JusGer | String(3000) | Sim | Justificativa geral p/ constar antes data emissão do  PPP |
| EmiJor | String(001) | Sim | Imprime jornada de trabalho mensal do colaborador no PPP |
| RquCNH | String(001) | Sim | Imprime requisito CNH no PPP |
| ExaPPR | String(001) | Sim | No PPP somente exame que conste no PPRA(laudo acima LT) |
| ExaTrf | Number(003,0) | Sim | Tempo a considerar de exames antes transferência(em dias) |
| MCatFP | String(011) | Sim | Modelo do Gerador Relatórios Default para CAT |
| ModLEP | String(011) | Sim | Modelo Relatório para listar EPIs distribuídos |
| AprCAT | String(001) | Sim | Critério para apresentação da CAT |
| LocAgt | String(001) | Sim | Apresentar o local da exposição ao perigo/fator risco |
| EncPer | String(001) | Sim | Define como os períodos mais atuais serão encerrados |
| IntLau | String(500) | Sim | Texto com a Introdução a ser utilizado no modelo LTCAT |
| AprCar | String(001) | Sim | Define qual título do cargo será apresentado no PPP (C/R) |
| AprGfi | String(002) | Sim | Expressão para apresentar GFIP em branco |
| AprCer | String(001) | Sim | Define qual CA deve ser apresentado, epi ou fornecedor(E/F) |
| AbrSit | String(025) | Sim | Tipos de anotações para compor as observações do PPP |
| CerEPI | String(001) | Sim | Considera nr. do CA, do EPI ou do fornecedor |
| DetCau | String(001) | Sim | No acidente, permite informar diversas causas |
| DetAge | String(001) | Sim | No acidente, permite informar diversos agentes causadores |
| DetLoc | String(001) | Sim | No acidente, permite informar diversos locais de lesões |
| DetNat | String(001) | Sim | No acidente, permite informar diversas naturezas de lesões |
| HisAfa | String(001) | Sim | Define se gera histórico no acidente com afastamento |
| AprFun | String(001) | Sim | Definição de como será apresentado o campo Função |
| AprSup | String(001) | Sim | No cadastro de reunião sugere o suplente como participante |
| ModPPP | String(011) | Sim | Modelo de relatório para listar o PPP |
| IdeEmp | String(001) | Sim | Identificação da Empresa no PPP |
| CATEmi | String(001) | Sim | Define para o PPP quais CATs listar |
| ExaSol | String(001) | Sim | Define como listar os Exames do Tipo Solicitação/Outros no PPP |
| AprLoc | String(001) | Sim | Define como será a apresentação do Local no PPP |
| LisLoc | String(001) | Sim | Define em que nível o Local será listado no PPP |
| UsaPSS | String(001) | Sim | Define se utiliza PSS |
| AprEpi | String(001) | Sim | Apresenta linha distinta p/cada EPI ou Concatena-os na mesma linha |
| TabEve | Number(003,0) | Sim | Código da tabela de eventos para os totalizadores |
| CodToT | Number(004,0) | Sim | Código do totalizador de horas trabalhadas |
| CodToA | Number(004,0) | Sim | Código do totalizador de horas de afastamento |
| CodReg | Number(003,0) | Sim | Código da regra para alterar nome do local na geração do PPP |
| AprObs | Number(001,0) | Sim | Define se apresenta e qual observação do Laudo apresenta |
| GerEst | String(001) | Sim | Gerar estabilidade para suplente(S/N) |
| InfSup | Number(001,0) | Sim | Indica quem poderá ser informado como suplente de outros membros |
| NumLot | Number(009,0) | Sim | Último nr. de lote gerado, alimentado pela distribuição coletiva |
| EpiNef | Number(001,0) | Sim | Define apresentação EPI/EPC eficaz, quando não aplicável |
| IdeAfa | Number(001,0) | Sim | Identificação do afastamento na emissão da CAT |
| ResFun | String(001) | Sim | Restringe funções da CIPA a  origem indicado/eleito(S/N) |
| IntOrd | String(8001) | Sim | Uso na emissão da OS (Introdução) |
| OriOrd | String(8001) | Sim | Uso na emissão da OS (Orientação de Segurança do Trabalho) |
| ProOrd | String(2000) | Sim | Uso na emissão da OS (Procedimentos em caso de Acidente de Trabalho) |
| TrmOrd | String(1000) | Sim | Uso na emissão da OS (Termo de Responsabilidade) |
| EpiCol | Number(001,0) | Sim | EPI por colaborador sobrepõe as demais definições(por empresa,local, etc.) |
| AprAtv | String(001) | Sim | Define se apresenta o cadastro de Atividades no CS |
| ModAte | String(011) | Sim | Modelo Relatório para Ata de Eleição da CIPA |
| ModAtr | String(011) | Sim | Modelo Relatório para Ata de Reunião da CIPA |
| ModAtp | String(011) | Sim | Modelo Relatório para Ata de Posse da CIPA |
| ObsCat | String(001) | Sim | Define quais observações serão listadas na emissão da CAT |
| BotAc1 | String(020) | Sim | Nome do 1º Botão para uso no cadastro do acidente |
| MBoAc1 | String(011) | Sim | Modelo gerador relatórios do 1º botão para uso no cadastro do acidente |
| RBoAc1 | Number(003,0) | Sim | Código da regra do 1º botão para uso no cadastro do acidente |
| BotAc2 | String(020) | Sim | Nome do 2º Botão para uso no cadastro do acidente |
| MBoAc2 | String(011) | Sim | Modelo gerador relatórios do 2º botão para uso no cadastro do acidente |
| RBoAc2 | Number(003,0) | Sim | Código da regra do 2º botão para uso no cadastro do acidente |
| BotAc3 | String(020) | Sim | Nome do 3º Botão para uso no cadastro do acidente |
| MBoAc3 | String(011) | Sim | Modelo gerador relatórios do 3º botão para uso no cadastro do acidente |
| RBoAc3 | Number(003,0) | Sim | Código da regra do 3º botão para uso no cadastro do acidente |
| AprAfa | String(001) | Sim | Define se apresenta os afastamentos no PPP |
| AbrTpS | String(100) | Sim | Tipos de situações de afastamento para considerar no PPP |
| NatLes | Number(001,0) | Sim | Indica a origem da informação do campo 60 - Descrição e Natureza da Lesão, da CAT. |
| DiaPro | Number(001,0) | Sim | Indica a origem da informação do campo 61 - Diagnóstico Provável, da CAT. |
| GerPen | String(001) | Sim | Gerar pendência para documento de protocolo de entrega de EPI |
| TipDoc | Number(004,0) | Sim | Tipo de documento para o protocolo de entrega de EPI |
| ModInv | String(011) | Sim | Modelo do Gerador Relatórios Default para Investigação de Ocorrências |
| BloPPP | String(001) | Sim | Define se registros importados podem ou não ser alterados |
| CerEqu | String(001) | Sim | Considerar CA do EPI equivalente |
| ADSOrd | String(001) | Sim | Indica se a descrição sumária do Cargo deve ser apresentada na Ordem de serviço |
| AAROrd | String(001) | Sim | Indica se as Atividades de risco serão apresentadas na Ordem de serviço |
| AROOrd | String(001) | Sim | Indica se os Riscos serão apresentados na Ordem de serviço |
| ConSup | Number(001,0) | Sim | Define a forma que relatórios e rotinas devem considerar os suplentes |
| AutEPI | Number(001,0) | Sim | Autenticação padrão na Entrega do EPI |
| FabBio | Number(002,0) | Sim | Fabricante da Leitora Biométrica |
| ConBio | Number(002,0) | Sim | Tipo de Conexão com a Leitora Biométrica |
| SrvBio | String(255) | Sim | Servidor da Leitora Biométrica |
| AprCAp | String(001) | Sim | Apresentação de CA no protocolo de entrega de EPI |
| ConLau | String(500) | Sim | Texto com a Conclusão a ser utilizado no modelo LTCAT |
| ModCCC | String(011) | Sim | Modelo do gerador relatórios padrão para Comprovante de Candidatura da CIPA |
| BtnMro | String(050) | Sim | Descrição do botão para uso na tela de Técnica de Avaliação de Riscos |
| ModMro | String(011) | Sim | Modelo de relatório para ser chamado na tela de Técnica de Avaliação de Riscos |
| BtnIro | String(050) | Sim | Descrição do botão para uso na tela de Inventário de Riscos |
| ModIro | String(011) | Sim | Modelo de relatório para ser chamado na tela de Inventário de Riscos |
| BotIRL | String(020) | Sim | Descrição do botão para uso na guia Inventário de Riscos da tela de Laudo |
| ModIRL | String(011) | Sim | Modelo a ser executado pelo botão da guia Inventário de Riscos da tela de Laudo |
| RegIRL | Number(003,0) | Sim | Regra a ser executada pelo botão da guia Inventário de Riscos da tela de Laudo |
| ColGHE | Number(001,0) | Sim | Indica como o sistema identificará os colaboradores ligados ao GHE |
| CmpGHE | Date | Sim | Competência de Ativação GHE de Colaborador por Posto |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086DEF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

