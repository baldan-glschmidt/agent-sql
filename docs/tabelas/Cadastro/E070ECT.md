# E070ECT

## Descrição

Cadastros - Empresas - Parâmetros Contabilidade

---

## Resumo

- Campos: 37
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtbLfd | String(001) | Não | Aceita lançamentos com filiais diferentes da informada no lote |
| OriRat | Number(001,0) | Não | Origem do rateio a ser considerado na contabilização |
| QtdCct | Number(003,0) | Sim | Quantidade de caracteres para limitar digitação da Descrição Conta Contábil |
| RegOri | String(001) | Sim | Registrar o movimento de origem do lançamento contábil |
| DesPar | String(001) | Sim | Descontabilizar o movimento de origem do lançamento na exclusão |
| MosCgc | String(001) | Sim | Habilitar o campo CNPJ/CPF nos lançamentos contábeis |
| ExiCgc | String(001) | Sim | Exigir que seja informado o CNPJ/CPF no lançamento contábil |
| LimTel | String(001) | Sim | Indicativo se deve limpar a tela de lançamento após o processamento |
| PerAlt | String(001) | Sim | Indicativo se permite alteração do lançamento contábil na consulta |
| AltVet | String(001) | Sim | Indicativo se permite alteração de lotes integrados do Vetorh |
| PrcMud | String(001) | Sim | Indicativo que a empresa esta em processo de mudança de plano de contas |
| CtbInt | String(001) | Sim | Indicativo que a empresa está habilitada para utilizar as rotinas de contabilidade internacional |
| MoeCnv | String(003) | Sim | Código da moeda de conversão utilizada na Contabilidade Internacional |
| AtuCnv | String(001) | Sim | Indicativo se irá atualizar automaticamente os lançamentos convertidos |
| CodMpr | Number(004,0) | Sim | Código do modelo de plano referencial padrão |
| UtiFtc | String(001) | Sim | Indicativo se utiliza fato contábil |
| QtdDia | Number(003,0) | Sim | Quantidade de dias para atualização da integração contábil por intervalo |
| QtdMov | Number(009,0) | Sim | Quantidade de movimentos por processamento na integração contábil |
| PcaCli | String(001) | Sim | Gerar conta de composição auxiliar ao cadastrar o cliente |
| PcdCli | String(001) | Sim | Gerar conta de composição auxiliar de adiantamento ao cadastrar o cliente |
| PcaFor | String(001) | Sim | Gerar conta de composição auxiliar ao cadastrar o fornecedor |
| PcdFor | String(001) | Sim | Gerar conta de composição auxiliar de adiantamento ao cadastrar o fornecedor |
| PcaCco | String(001) | Sim | Gerar conta de composição auxiliar ao cadastrar a conta interna (tesouraria) |
| PftJin | String(001) | Sim | Processar fato contábil junto à integração contábil |
| ConGrp | String(001) | Sim | Controle de contas geral e rural individual |
| HpcEc1 | Number(004,0) | Sim | Historico Padrão Entrada de Distribuição de Custo 1 |
| HpcEc2 | Number(004,0) | Sim | Historico Padrão Entrada de Distribuição de Custo 2 |
| HpcSc1 | Number(004,0) | Sim | Historico Padrão Saída de Distribuição de Custo 1 |
| HpcSc2 | Number(004,0) | Sim | Historico Padrão Saída de Distribuição de Custo 2 |
| HpdTcf | Number(004,0) | Sim | Historico Padrão Zeramento Contábil Custos |
| HpdTgf | Number(004,0) | Sim | Historico Padrão de Transf. Gastos por filial |
| DatCis | Date | Sim | Data da Última Cisão |
| DatReg | Date | Sim | Data da Última Mudança do Regime |
| RegTra | String(001) | Sim | Indica qual o regime tributário atual do IRPJ/CSLL |
| VisPat | String(020) | Sim | Visão Balanço Patrimonial utilizada para integração com o Analytics |
| VisDre | String(020) | Sim | Visão Demostração Resultado do Exercício utilizada para integração com o Analytics |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
