# R350SVA

## Descrição

S-2306 - eSocial - Trabalhador Sem Vínculo de Emprego/Estatutário - Alt. Contratual

---

## Resumo

- Campos: 65
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqSva | Number(009,0) | Não | Sequência |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| MatTra | String(030) | Sim | Matrícula do Trabalhador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| DatAlt | Date | Sim | Data da alteração das informações |
| NatAti | Number(001,0) | Sim | Natureza da atividade |
| CodCar | String(030) | Sim | Código do Cargo |
| DesCar | String(100) | Sim | Descrição do cargo |
| CodCbo | String(006) | Sim | Cbo 2002 do Cargo |
| CodFun | String(030) | Sim | Código da função |
| DesFun | String(100) | Sim | Descrição da função |
| CboFun | String(006) | Sim | Cbo 2002 da Função |
| SalFix | Number(014,2) | Sim | Salário fixo |
| UndFix | Number(001,0) | Sim | Unidade de pagamento da parte fixa da remuneração |
| DesVar | String(999) | Sim | Descrição do salário variável |
| RemCar | String(001) | Sim | Indicar se o servidor optou pela remuneração do cargo efetivo |
| RegPre | Number(002,0) | Sim | Tipo de regime previdenciário |
| NatEst | String(001) | Sim | Natureza do estágio |
| NivEst | Number(001,0) | Sim | Nível do estágio |
| AreAtu | String(100) | Sim | Área de atuação do estagiário |
| ApoSeg | String(030) | Sim | Número Apólice de Seguro |
| VlrBol | Number(014,2) | Sim | Valor da bolsa, se o estágio for remunerado |
| DatTer | Date | Sim | Data prevista para o término do estágio |
| EmpEns | Number(014,0) | Sim | CNPJ da instituição de ensino |
| CfjEns | String(014) | Sim | CNPJ da instituição de ensino |
| NomEns | String(100) | Sim | Nome do contribuinte (pessoa física) ou a razão social (pessoa jurídica) |
| EndEns | String(100) | Sim | Descrição do logradouro |
| NumEns | String(010) | Sim | Número do logradouro |
| BaiEns | String(090) | Sim | Nome do bairro/distrito |
| CEPEns | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunEns | Number(007,0) | Sim | Código do município |
| EstEns | String(002) | Sim | Sigla da Unidade da Federação |
| EmpAge | Number(014,0) | Sim | CNPJ do agente de integração |
| CfjAge | String(014) | Sim | CNPJ do agente de integração |
| NomAge | String(100) | Sim | Nome do contribuinte (pessoa física) ou a razão social (pessoa jurídica) |
| EndAge | String(080) | Sim | Descrição do logradouro |
| NumAge | String(010) | Sim | Número do logradouro |
| BaiAge | String(060) | Sim | Nome do bairro/distrito |
| CEPAge | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunAge | Number(007,0) | Sim | Código do município |
| EstAge | String(002) | Sim | Sigla da Unidade da Federação |
| CpfSup | Number(011,0) | Sim | CPF do responsável pela supervisão do estagiário |
| NomSup | String(070) | Sim | Nome do Supervisor do Estágio |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Determina se envio é válido |
| EnvExc | String(001) | Sim | Envio Excluído |
| TinLoc | Number(001,0) | Sim | Tipo de inscrição do estabelecimento |
| NinLoc | Number(014,0) | Sim | Número de inscrição do estabelecimento |
| CfjLoc | String(014) | Sim | Número de inscrição do estabelecimento |
| DesLoc | String(080) | Sim | Descrição complementar do local de trabalho |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqSva

---

## Índices

### R350SVAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
