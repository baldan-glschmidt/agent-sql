# E095FOR_REC

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Fornecedores

---

## Resumo

- Campos: 128
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcCpf | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIde | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| CodFor | Number(009,0) | Não | Código do Fornecedor gerado no ERP |
| NomFor | String(100) | Não | Nome do fornecedor |
| ApeFor | String(050) | Não | Nome fantasia do fornecedor |
| MarFor | String(020) | Sim | Marca do fornecedor |
| SenFor | String(010) | Sim | Senha do Fornecedor |
| TipFor | String(001) | Não | Tipo de Fornecedor |
| TipMer | String(001) | Não | Tipo de Mercado do fornecedor |
| CodRam | String(005) | Sim | Código do ramo de atividade |
| InsEst | String(025) | Sim | Inscrição estadual do fornecedor |
| InsMun | String(016) | Sim | Inscrição municipal do fornecedor |
| CodGre | Number(009,0) | Sim | Código do grupo de empresas |
| CodSuf | String(010) | Sim | Código na suframa |
| EndFor | String(100) | Sim | Endereço do fornecedor |
| CplEnd | String(200) | Sim | Complemento do endereço do fornecedor (sala, andar, etc.) |
| BaiFor | String(075) | Sim | Bairro do fornecedor |
| ZipCod | String(014) | Sim | Código da cidade do fornecedor externo - ZIP CODE |
| CepFor | Number(008,0) | Sim | CEP do fornecedor |
| CepIni | Number(008,0) | Sim | Faixa inicial do CEP da cidade do fornecedor |
| CidFor | String(060) | Sim | Cidade do fornecedor |
| SigUfs | String(002) | Sim | Estado do fornecedor |
| FonFor | String(020) | Sim | Número do telefone - 1 |
| FonFo2 | String(020) | Sim | Número do telefone - 2 |
| FonFo3 | String(020) | Sim | Número do telefone - 3 |
| FaxFor | String(020) | Sim | Número do FAX do fornecedor |
| CxaPst | Number(006,0) | Sim | Número da caixa postal do fornecedor |
| IntNet | String(100) | Sim | Endereço eletrônico (E-Mail) |
| NomVen | String(030) | Sim | Nome do vendedor ou representante autorizado do fornecedor |
| FonVen | String(020) | Sim | Número do telefone do vendedor ou representante do fornecedor |
| RmlVen | Number(004,0) | Sim | Número do ramal do vendedor ou representante do fornecedor |
| FaxVen | String(020) | Sim | Número do FAX do vendedor ou representante do fornecedor |
| CodCli | Number(009,0) | Sim | Código do fornecedor como cliente |
| TipFav | String(001) | Sim | Tipo de fornecedor de agência de viagem |
| CodIac | Number(004,0) | Sim | Código IATA da cia. aérea |
| AbrIac | String(004) | Sim | Abreviação IATA da cia. aérea |
| IndBsp | String(001) | Sim | Indicativo se a cia. aérea pertence ao BSP |
| CodAma | String(030) | Sim | Código do fornecedor no Amadeus |
| CodSab | String(030) | Sim | Código do fornecedor no Sabre |
| CodGal | String(030) | Sim | Código do fornecedor no Galileo |
| TipMho | String(001) | Sim | Tipo de meio de hospedagem |
| CodCth | String(005) | Sim | Categoria do meio de hospedagem |
| UsuCad | Number(010,0) | Sim | Usuário responsável pelo cadastramento |
| DatCad | Date | Sim | Data do cadastramento do fornecedor |
| HorCad | Number(005,0) | Sim | Hora/minuto do cadastramento do fornecedor |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| SitFor | String(001) | Não | Situação do fornecedor |
| CodMot | Number(006,0) | Sim | Código do motivo da situação do fornecedor |
| ObsMot | String(250) | Sim | Observação do motivo da situação do fornecedor |
| UsuMot | Number(010,0) | Sim | Usuário responsável pelo motivo da situação do fornecedor |
| DatMot | Date | Sim | Data do motivo da situação do fornecedor |
| HorMot | Number(005,0) | Sim | Hora do motivo da situação do fornecedor |
| CodPai | String(004) | Sim | Código do país do fornecedor |
| ForRep | Number(009,0) | Sim | Código do fornecedor como representante |
| ForTra | Number(009,0) | Sim | Código do fornecedor como transportadora |
| NotSis | Number(005,2) | Sim | Nota para o sistema da qualidade do Fornecedor |
| NotFor | Number(005,2) | Sim | Nota dos fornecimentos deste fornecedor |
| CodTri | String(005) | Sim | Código de tributação para emissão de DARF/DIRF |
| GerDir | String(001) | Sim | Indicativo se devem ser exportados os dados do fornecedor para DIRF |
| CliFor | String(001) | Sim | Indicativo se o registro representa um cliente ou um fornecedor ou ambos |
| IdeFor | String(020) | Sim | Código para identificação do fornecedor |
| QtdDep | Number(004,0) | Sim | Quantidade de dependentes do Fornecedor |
| TemOrm | String(001) | Sim | Indicativo se o fornecedor tem endereços de origem da mercadoria |
| RecPis | String(001) | Sim | Indicativo se as notas fiscais do fornecedor poderão ter recuperação de PIS |
| PerPid | Number(007,4) | Sim | Percentual de recuperação de PIS diferenciado para o fornecedor |
| TriIss | String(001) | Sim | Indicativo se o fornecedor tributa ISS |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para integração |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| NotAfo | Number(005,2) | Sim | Nota da Avaliação do fornecedor |
| TipInt | Number(001,0) | Sim | Tipo de Integração |
| CodRoe | String(003) | Sim | Código da Rota ou Localidade do Fornecedor |
| SeqRoe | Number(004,0) | Sim | Sequência da rota ou localidade |
| RecCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de Cofins |
| PerCod | Number(007,4) | Sim | Percentual de recuperação de Cofins diferenciado |
| RetCof | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de Cofins |
| RetCsl | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de CSLL |
| RetPis | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de PIS |
| RetOur | String(001) | Sim | Indicativo se as notas fiscais poderão ter Outras Retenções |
| CodSro | String(003) | Sim | Código da Sub Rota |
| RecIpi | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de IPI |
| RecIcm | String(001) | Sim | Indicativo se as notas fiscais poderão ter recuperação de ICMS |
| TriIcm | String(001) | Sim | Indicativo se o fornecedor tem tributação de ICMS ou não |
| TriIpi | String(001) | Sim | Indicativo se o fornecedor tem tributação de IPI ou não |
| RetPro | String(001) | Sim | Indicativo se o fornecedor controla retenções |
| RetIrf | String(001) | Sim | Indicativo se as notas fiscais poderão ter retenção de IRRF |
| IndFor | String(001) | Sim | Indicativo do tipo do fornecedor |
| LimRet | String(001) | Sim | Indicativo de como é utilizado o valor limite para cálculos de retenção |
| EenFor | String(018) | Sim | Código do endereço do fornecedor |
| NumRge | String(013) | Sim | Número do documento de identidade (RG) do fornecedor |
| ForWms | String(015) | Sim | Código do fornecedor no sistema de WMS |
| PerRir | Number(005,2) | Sim | Percentual de redução do valor base IRRF na baixa dos títulos |
| PerRin | Number(005,2) | Sim | Percentual de redução do valor base INSS na baixa dos títulos |
| NenFor | String(060) | Sim | Número do endereço do fornecedor |
| EmaNfe | String(100) | Sim | Endereço eletrônico (E-Mail) para envio de arquivos de documentos eletrônicos |
| InsAnp | Number(007,0) | Sim | Código da instalação conforme cadastro da ANP |
| IndCoo | String(001) | Sim | Indicativo se cliente/fornecedor é cooperado. |
| CodRtr | Number(001,0) | Sim | Código do Regime Tributário |
| RegEst | Number(002,0) | Sim | Regime Especial de Tributação (Meramente Informativo para NF-e) |
| RotAnx | Number(002,0) | Sim | Código da rotina para controle de arquivos anexos |
| NumAnx | Number(010,0) | Sim | Número do controle de arquivos anexos gerado pelo sistema |
| TipPgt | String(002) | Sim | Tipo de pagamento do título |
| PerIcm | Number(007,4) | Sim | Percentual do ICMS nas NFE dos forn. com regime tributário simples nacional |
| NumIdf | String(040) | Sim | Número de identificação fiscal |
| SusRor | String(001) | Sim | Indicativo se o fornecedor está suspenso por registro de ocorrência |
| AgrDes | Number(005,2) | Sim | Percentual de deságio para pagamento do crédito do ICMS no agronegócio |
| EndNet | String(200) | Sim | Endereço do site do fornecedor |
| TipEmp | Number(002,0) | Sim | Tipo de empresa |
| PerRed | String(001) | Sim | Indicativo se o fornecedor permite redução de base de IRRF |
| EntPaa | String(001) | Sim | Entidade inscrita no Programa de Aquisição de Alimentos (PAA) |
| IndNif | Number(001,0) | Sim | Indicativo do Número de Identificação Fiscal |
| DatLau | Date | Sim | Data do laudo para portador de moléstia grave |
| TipCdf | Number(001,0) | Sim | Tipo de cálculo do ICMS diferido |
| GenA01 | String(080) | Sim | Tratamentos externos ao ERP no fornecedor da nota - A1 |
| GenA02 | String(080) | Sim | Tratamentos externos ao ERP no fornecedor da nota - A2 |
| GenA03 | String(080) | Sim | Tratamentos externos ao ERP no fornecedor da nota - A3 |
| GenA04 | String(080) | Sim | Tratamentos externos ao ERP no fornecedor da nota - A4 |
| GenA05 | String(080) | Sim | Tratamentos externos ao ERP no fornecedor da nota - A5 |
| GenA06 | String(080) | Sim | Tratamentos externos ao ERP no fornecedor da nota - A6 |
| GenN01 | Number(013,2) | Sim | Tratamentos externos ao ERP no fornecedor da nota - N1 |
| GenN02 | Number(013,2) | Sim | Tratamentos externos ao ERP no fornecedor da nota - N2 |
| GenN03 | Number(013,2) | Sim | Tratamentos externos ao ERP no fornecedor da nota - N3 |
| GenN04 | Number(013,2) | Sim | Tratamentos externos ao ERP no fornecedor da nota - N4 |
| GenN05 | Number(013,2) | Sim | Tratamentos externos ao ERP no fornecedor da nota - N5 |
| GenN06 | Number(013,2) | Sim | Tratamentos externos ao ERP no fornecedor da nota - N6 |
| IdeUni | String(050) | Não | Identificador único alfanumérico |

---

## Chave Primária

- IdeUni

---

## Índices

### E095FOR_RECIndice1

**Tipo:** Não unico

Campos:
- DocIde

### E095FOR_RECIndice2

**Tipo:** Não unico

Campos:
- CgcCpf

---

## Relacionamentos

Nenhum relacionamento cadastrado.
