# R030DES

## Descrição

Definições do eSocial

---

## Resumo

- Campos: 60
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| DatUes | Date | Sim | Início Tabelas |
| TerSis | Date | Sim | Data em que a empresa trocou de sistema |
| TerUes | Date | Sim | Data de encerramento das atividades da empresa no eSocial |
| GerLot | Number(001,0) | Sim | Geração Lotação |
| OldLot | Number(001,0) | Sim | Lotação Anterior |
| UltMat | Number(010,0) | Sim | Última Matrícula |
| DatPen | Date | Sim | Data Pendência |
| DtGFIP | Date | Sim | Comp. Substituição GFIP |
| AbrIse | String(200) | Sim | Totalizador Isento |
| IdeEmp | String(008) | Sim | Identificador empresa |
| TipAmb | Number(001,0) | Sim | Tipo de Ambiente eSocial |
| DatTab | Date | Sim | Data de início das tabelas |
| FunEso | Number(001,0) | Sim | Função eSocial |
| EmpDom | String(001) | Sim | S-1000 enviado pelo Portal Doméstica |
| ConInd | String(001) | Sim | Enviar Contr. Individual Opcionais S-2300 (S,N) |
| DetNfe | String(001) | Sim | Enviar Detalhamento de Notas Fiscais de comercialização de produção (S,N) |
| EnvObs | String(001) | Sim | Enviar Observações Eventos S-1010 |
| EnvIpe | String(001) | Sim | Enviar Incidências CPRP Eventos S-1010 |
| HorCon | String(001) | Sim | Enviar o grupo Horário Contratual nos leiautes S-2200 e S-2206 (S,N) |
| FecFol | String(001) | Sim | Realizar Consistência Fechamento Folha de Pagamento S-1299 (S,N) |
| EnvPla | Number(001,0) | Sim | Enviar Plano de Saúde S-1200/S-2299/S-2399 |
| BasDes | Number(001,0) | Sim | Base Descentralizada |
| BasSeq | Number(004,0) | Sim | Identificador da Base Descentralizada |
| IniNpe | Date | Sim | Data de início do eSocial (Não Periódicos) |
| IniPer | Date | Sim | Data de início do eSocial (Periódicos) |
| OpcDis | Number(001,0) | Sim | Opção Dissídio S-2206 |
| PrxVer | Date | Sim | Informar a Data de Início da Versão 2.5 do eSocial |
| CarFun | String(001) | Sim | Enviar os grupos Cargo e Função no S-2300 e S-2306 para as categorias 901, 903, 904 e 905 (S,N) |
| RemCpl | String(001) | Sim | Enviar o grupo Remuneração no S-2300 e S-2306 para as categorias em que é opcional (S,N) |
| IniSST | Date | Sim | Data de início da obrigatoriedade dos eventos de SST |
| InSST2 | Date | Sim | Data de início da obrigatoriedade dos eventos de SST (Fase 2) |
| IniDct | Date | Sim | Data de início DCTFWeb |
| IniGrf | Date | Sim | Data de início GRFGTS - obsoleto |
| SenAlt | String(030) | Sim | Senha Alteração Data Versão no eSocial |
| ConPar | String(001) | Sim | Considerar parceiros nos eventos de Segurança e Saúde no Trabalho (SST) |
| ResExa | String(001) | Sim | Enviar a informação do resultado do exame no evento S-2220 (S,N) |
| GerEvt | Number(001,0) | Sim | Informar quais eventos devem ser gerados (eventos de folha e/ou eventos de SST) |
| ConHsa | String(001) | Sim | Valor complemento de hist. salarial considera para S-2200/S-2206/S-2300/S-2306 |
| InfFac | Number(001,0) | Sim | Informar se as informações facultativas devem ser enviadas para o eSocial |
| OrdFiL | Number(001,0) | Sim | Ordem de preferência de busca de filial para lotação |
| AgeAfa | String(001) | Sim | Agendar S-2230 |
| SimFol | Date | Sim | Data de Início Simplificação eSocial |
| MosPre | String(001) | Sim | Mostrar Pesquisa Registro Preliminar |
| ManBen | Number(001,0) | Sim | Manutenção Benefícios Ente Público |
| IndGui | String(001) | Sim | Indicativo de guia |
| IniS11 | Date | Sim | Data Início Versão Simplificada 1.1 |
| CmpAu1 | Date | Sim | Campo Auxiliar 1 |
| CmpAu2 | Date | Sim | Campo Auxiliar 2 |
| CmpAu3 | String(001) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(004,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Number(011,2) | Sim | Campo Auxiliar 5 |
| CmpAu6 | String(2000) | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(2000) | Sim | Campo Auxiliar 7 |
| EnvCat | Number(001,0) | Sim | Módulo responsável pela geração e envio do evento S-2210 (SM e/ou AP) |
| IniS12 | Date | Sim | Data Início Versão Simplificada 1.2 |
| DatMig | Date | Sim | Início da migração do eSocial |
| IniS13 | Date | Sim | Data início versão S-1.3 |
| TipDes | Number(001,0) | Sim | Descrição do Cargo |
| EnvExa | Number(001,0) | Sim | Módulo responsável pela geração e envio do evento S-2221 (SM e/ou AP) |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
