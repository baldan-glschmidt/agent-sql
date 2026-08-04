# E073MOT

## Descrição

Cadastros - Transportadoras - Motoristas

---

## Resumo

- Campos: 47
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| CodMtr | Number(006,0) | Não | Código do Motorista |
| NomMot | String(100) | Não | Nome do motorista |
| CgcCpf | Number(012,0) | Sim | Número do CPF do motorista |
| EndMot | String(100) | Sim | Endereço do motorista |
| CplEnd | String(200) | Sim | Complemento do endereço do motorista (sala, andar, etc.) |
| BaiMot | String(075) | Sim | Bairro do motorista |
| CepMot | Number(008,0) | Sim | CEP do motorista |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade do motorista |
| CidMot | String(060) | Sim | Cidade do motorista |
| SigUfs | String(002) | Sim | Estado do motorista |
| FonMot | String(020) | Sim | Número do telefone - 1 |
| FonMo2 | String(020) | Sim | Número do telefone - 2 |
| FaxMot | String(020) | Sim | Número do FAX do motorista |
| CxaPst | Number(006,0) | Sim | Número da caixa postal do motorista |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| UsuCad | Number(010,0) | Sim | Usuário responsável pelo cadastramento |
| DatCad | Date | Sim | Data do cadastramento do motorista |
| HorCad | Number(005,0) | Sim | Hora/minuto do cadastramento |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| SitMot | String(001) | Não | Situação do motorista |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do motorista |
| ObsMot | String(250) | Sim | Observação do motivo da situação |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação |
| DatMot | Date | Sim | Data do motivo da situação |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação |
| CodPai | String(004) | Sim | Código do país |
| MotFor | Number(009,0) | Sim | Código do motorista como fornecedor |
| NumCnh | String(030) | Sim | Habilitação do motorista |
| VldCnh | Date | Sim | Validade da Habilitação do motorista |
| EmiCnh | Date | Sim | Emissão da Habilitação do motorista |
| CatCnh | String(002) | Sim | Categoria da habilitação do motorista |
| NumRge | String(013) | Sim | Número do RG (Identidade) |
| OrgRge | String(006) | Sim | Órgão emissor do RG |
| DatRge | Date | Sim | Data de emissão do RG |
| DatNas | Date | Sim | Data do nascimento do motorista |
| ConMot | String(001) | Sim | Conceito do Motorista |
| SitLis | String(001) | Sim | Situação do Check List |
| NumPro | String(015) | Sim | Número do prontuário |
| EenMot | String(018) | Sim | Código do endereço do motorista |
| NenMot | String(060) | Sim | Número do endereço do motorista |
| MetMot | Number(004,0) | Sim | Meta de entregas do motorista no período |
| VctMet | Number(004,0) | Sim | Data limite para o fechamento da meta mensal de entregas |
| PerCom | Number(005,2) | Sim | Percentual de comissão a ser pago ao motorista quando ultrapassar a meta |
| NumIdf | String(040) | Sim | Número de identificação fiscal |

---

## Chave Primária

- CodTra
- CodMtr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
