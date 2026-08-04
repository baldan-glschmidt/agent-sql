# E000CSE

## Descrição

Integrações - Varejo - Controle de Séries Externas

---

## Resumo

- Campos: 57
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| NumSep | String(050) | Não | Número de série do produto |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| CodDep | String(010) | Não | Código do depósito a ser baixado o estoque do produto |
| SerExt | Number(009,0) | Não | Código Série Externa utilizada pelo parceiro |
| NumExt | String(016) | Não | Número Controle Externo utilizado pelo parceiro |
| TipCur | Number(001,0) | Não | Tipo Curso Externo recebido do parceiro |
| SerFil | Number(005,0) | Sim | Código da filial do pedido, pré-fatura ou nota fiscal |
| DepFil | String(010) | Sim | Depósito na filial |
| DatTrf | Date | Sim | Data da transferência da série para as filiais |
| QtdEst | Number(014,5) | Sim | Quantidade que compõe o registro |
| EmpNfc | Number(004,0) | Sim | Código da empresa |
| FilNfc | Number(005,0) | Sim | Código da filial |
| NumNfc | Number(009,0) | Sim | Número da nota fiscal de entrada |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |
| EmpNfv | Number(004,0) | Sim | Código da empresa |
| FilNfv | Number(005,0) | Sim | Código da filial |
| SnfNfv | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |
| DatGer | Date | Sim | Data Geração |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitSer | Number(001,0) | Sim | Situação Série recebida pelo parceiro |
| DatCad | Date | Sim | Data do cadastro do registro |
| DatCan | Date | Sim | Data cancelamento do registro |
| SitReg | Number(001,0) | Sim | Indicativo da situação do registro |
| NomCli | String(100) | Sim | Nome do cliente |
| IdeCli | String(015) | Sim | Número do CNPJ ou CPF do cliente |
| EndCli | String(100) | Sim | Endereço do cliente |
| NunEnt | String(020) | Sim | Número endereço do cliente |
| CplEnd | String(200) | Sim | Complemento do endereço do cliente (sala, andar, etc.) |
| BaiCli | String(075) | Sim | Bairro do cliente |
| CidCli | String(060) | Sim | Cidade do cliente |
| SigUfs | String(002) | Sim | Sigla do estado do cliente |
| CepEnd | String(008) | Sim | CEP do cliente |
| FonCli | String(020) | Sim | Número do telefone - 1 |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| CodRep | Number(009,0) | Sim | Código do representante |
| NomRep | String(100) | Sim | Nome do representante |
| IdeFil | String(015) | Sim | Identidade da filial |
| NomFil | String(100) | Sim | Nome da filial |
| IdeReg | String(050) | Sim | Identidade da regional |
| NomReg | String(050) | Sim | Nome da regional |
| PedPar | String(050) | Sim | Pedido do parceiro |
| DatVen | Date | Sim | Data da Venda |
| CodPed | String(050) | Sim | ID Pedido interno |
| MotRet | Number(006,0) | Sim | Código do motivo no retorno |
| DesRet | String(050) | Sim | Descrição no retorno |
| EmpDev | Number(004,0) | Sim | Código da empresa |
| FilDev | Number(005,0) | Sim | Código da filial |
| NfcDev | Number(009,0) | Sim | Número da nota fiscal de entrada |
| SnfDev | String(003) | Sim | Código da série da nota fiscal de entrada |
| IpcDev | Number(003,0) | Sim | Sequência do item na nota fiscal de entrada |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- NumSep
- CodFor

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
