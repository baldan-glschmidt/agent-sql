# E140DCF

## Descrição

Vendas - Notas Fiscais de Saída - Dados Gerais - Dados Cupom Fiscal

---

## Resumo

- Campos: 25
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| TipCli | String(001) | Sim | Tipo do cliente |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do cliente |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do cliente |
| NomCli | String(100) | Sim | Nome do cliente |
| SeqHas | Number(009,0) | Sim | Sequencia do hash para controle de alteração de registro para PAF-ECF |
| NumPsp | String(040) | Sim | Número do passaporte do cliente |
| InsEst | String(025) | Sim | Inscrição estadual do cliente |
| InsMun | String(016) | Sim | Inscrição municipal do cliente |
| EndCli | String(100) | Sim | Endereço do cliente |
| CplEnd | String(200) | Sim | Complemento do endereço do cliente (sala, andar, etc.) |
| CepCli | Number(008,0) | Sim | CEP do cliente |
| BaiCli | String(075) | Sim | Bairro do cliente |
| CidCli | String(060) | Sim | Cidade do cliente |
| SigUfs | String(002) | Sim | Sigla do estado do cliente |
| CodPai | String(004) | Sim | Código do país do cliente |
| FonCli | String(020) | Sim | Número de Telefone |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| ObsCli | String(1000) | Sim | Observação |
| NumRge | String(013) | Sim | Número da Identidade |
| CodSuf | String(010) | Sim | Código na suframa |
| TipMer | String(001) | Sim | Tipo de mercado do cliente |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140DCF_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

