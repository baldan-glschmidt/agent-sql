# E073TRA

## Descrição

Cadastros - Transportadoras

---

## Resumo

- Campos: 50
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTra | Number(009,0) | Não | Código da Transportadora |
| NomTra | String(100) | Não | Nome da transportadora |
| ApeTra | String(050) | Não | Nome fantasia da transportadora |
| TipTra | String(001) | Não | Tipo de transportadora |
| InsEst | String(025) | Sim | Inscrição estadual da transportadora |
| InsMun | String(016) | Sim | Inscrição municipal da transportadora |
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF da transportadora |
| DocIdeTra | String(014) | Sim | Número do CNPJ ou CPF da transportadora |
| EndTra | String(100) | Sim | Endereço da transportadora |
| CplEnd | String(200) | Sim | Complemento do endereço da transportadora (sala, andar, etc.) |
| CepTra | Number(008,0) | Sim | Cep da transportadora |
| BaiTra | String(075) | Sim | Bairro da transportadora |
| CidTra | String(060) | Sim | Cidade da transportadora |
| SigUfs | String(002) | Sim | Sigla do estado da transportadora |
| NomCto | String(150) | Sim | Nome da pessoa de contato na transportadora |
| FonTra | String(020) | Sim | Número do telefone da transportadora |
| FaxTra | String(020) | Sim | Número do FAX da transportadora |
| CxaPst | Number(006,0) | Sim | Número da caixa postal da transportadora |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| CodVia | String(003) | Não | Código da via de transporte da transportadora |
| PlaVei | String(010) | Sim | Placa do veículo principal da transportadora |
| CifFob | String(001) | Não | Indicativo se o frete da transportadora é CIF ou FOB |
| TraCli | Number(009,0) | Sim | Código da transportadora como cliente |
| TraFor | Number(009,0) | Sim | Código da transportadora como fornecedor |
| SitTra | String(001) | Não | Situação da transportadora |
| PesMax | Number(011,2) | Sim | Peso Máximo para frota própria |
| VolMax | Number(011,2) | Sim | Volume Máximo para Frota Própria |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| EenTra | String(018) | Sim | Código do endereço da transportadora |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| PagCle | String(001) | Sim | Tipo de pagamento do serviço de coleta |
| NenTra | String(060) | Sim | Número do endereço da transportadora |
| NrnTrc | String(014) | Sim | Registro nacional de transportadores rodoviários de carga - RNTRC |
| CodPai | String(004) | Sim | Código do país da transportadora |
| VlrKmt | Number(015,2) | Sim | Valor pago por quilômetro utilizado |
| ProTra | Number(001,0) | Sim | Tipo proprietário para atender mdf-e |
| TpoTra | Number(001,0) | Sim | Tipo transportador para atender mdf-e |
| NumIdf | String(040) | Sim | Número de identificação fiscal |
| CodTaf | String(012) | Sim | Termo de Autorização dos Serviços em Regime de Fretamento - TAF |
| NroRes | String(025) | Sim | Número de registro adquirido junto a Administração Estadual. |
| USU_NumRec | Number(005,0) | Sim | Numero do Recibo |
| USU_IntSF | String(001) | Sim | Integra com Salesforce |

---

## Chave Primária

- CodTra

---

## Índices

### E073TRAIndice1

**Tipo:** Não unico

Campos:
- CodVia

---

## Relacionamentos

### IR_E073TRA_019

**Tabela:** E074VIA

| Origem | Destino |
|--------|---------|
| CodVia | CodVia |

