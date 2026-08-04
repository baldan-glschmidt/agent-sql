# E205DEP

## Descrição

Estoques - Depósitos - Cadastro

---

## Resumo

- Campos: 45
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDep | String(010) | Não | Código do depósito |
| DesDep | String(030) | Não | Descrição do depósito |
| AbrDep | String(010) | Não | Abreviatura do depósito |
| TipDep | Number(001,0) | Não | Tipo de depósito/localização |
| CodMde | Number(004,0) | Sim | Código da máscara de depósito |
| MskDep | String(018) | Sim | Máscara do depósito |
| NivDep | Number(001,0) | Sim | Nível do depósito conforme a máscara |
| QtdPos | Number(001,0) | Sim | Quantidade de posições do nível da máscara de depósito |
| PriBus | Number(006,0) | Sim | Prioridade de busca no depósito/localização |
| CpmDep | Number(008,3) | Sim | Comprimento do depósito/localização |
| LarDep | Number(008,3) | Sim | Largura do depósito/localização |
| AltDep | Number(008,3) | Sim | Altura do depósito/localização |
| CapPes | Number(009,3) | Sim | Capacidade em peso do depósito/localização |
| CapVol | Number(009,3) | Sim | Capacidade em volume do depósito/localização |
| CodFil | Number(005,0) | Não | Código da filial que o depósito pertence |
| DepCpr | String(001) | Não | Indicativo se o depósito é comprador |
| EstNeg | String(001) | Não | Indicativo se o depósito aceita saldo de estoque negativo |
| DisXpl | String(001) | Não | Considera (S=Sim/N=Não) produtos deste depósito p/ o Cálculo de Necessidades avaliar o estoque disponível (Explosão Nec.) |
| IndClt | String(001) | Não | Indica se o depósito é de coleta (Permite faturar somente de depósitos de coleta) |
| CodCcu | String(009) | Sim | Código do Centro de Custo associado ao depósito p/ apuração dos valorização dos estoques por depósito |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| SitDep | String(001) | Não | Situação do depósito |
| ObsDep | String(250) | Sim | Texto da observação do Depósito |
| SeqDep | Number(004,0) | Sim | Sequência do Depósito para separação de mercadorias |
| GerEmb | String(001) | Sim | Indicativo se são geradas embalagens de estocagem para o produto |
| ConAep | String(001) | Sim | Indicativo se considera o depósito na análise de estoque para atendimento do pedido |
| DepVen | String(001) | Sim | Indicativo se o depósito é vendedor |
| DepIql | String(001) | Sim | Indicativo se o depósito é utilizado para inspeções do SGQ |
| InvEmb | String(001) | Sim | Indicativo se o depósito está em processo de inventário de embalagens |
| IntWms | String(001) | Sim | Indicativo se o depósito integra com o sistema de WMS |
| MsgEsn | String(001) | Sim | Exibir mensagem de estoque negativo |
| DepVir | String(001) | Sim | Identificar se depósito é virtual |
| CriOrd | Number(004,0) | Sim | Critério de ordenação para formação das pré-faturas |
| IntWmw | String(001) | Sim | Indicativo se registro deve integrar com o WMW |
| IntPos | String(001) | Sim | Indicativo se o registro integra no Gestão Safra |
| CodImr | Number(009,0) | Sim | Identificação do imóvel |
| SitWmw | String(001) | Sim | Situação do registro no WMW |
| USU_nomenc | String(030) | Sim | Nome Encarregado |
| USU_IntSF | String(001) | Sim | Integra com Salesforce |
| USU_NomSet | String(030) | Sim | Nome Setor Deposito |

---

## Chave Primária

- CodEmp
- CodDep

---

## Índices

### E205DEPIndice2

**Tipo:** Não unico

Campos:
- TipDep
- CodEmp
- PriBus
- CodDep

### E205DEPIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil

---

## Relacionamentos

### IR_E205DEP_015

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

