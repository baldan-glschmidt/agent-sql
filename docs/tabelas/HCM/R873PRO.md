# R873PRO

## Descrição

Integração de dados Portuários

---

## Resumo

- Campos: 61
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SEQUENCIAL | Number(010,0) | Não | Número sequencial do processo de solicitação |
| CNPJ | Number(015,0) | Sim | CNPJ da pessoa jurídica - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ da pessoa jurídica |
| REPROCESSAMENTO | String(003) | Sim | Indica se a informação está sendo reprocessada. |
| JURISDICAO | String(010) | Sim | Jurisdição ao qual a informação se refere. |
| TIPOREGISTRO | String(003) | Sim | Corresponde a sigla da solicitação de processamento |
| VERSAO | Number(003,0) | Sim | Versão. Valor fixo 001. |
| CODIGOERRO | Number(005,0) | Sim | Código do status do processamento. |
| DESCRICAOERRO | String(100) | Sim | Descrição do status do processamento. |
| TIPDOCREP | String(003) | Sim | Tipo do documento do Representante Legal  da PJ. |
| DOCREP | String(020) | Sim | Documento do Representante Legal da PJ. |
| EXECUTOR | Number(011,0) | Sim | Número do CPF do usuário que efetuou o processamento |
| OPERACAO | String(003) | Sim | Operação que está sendo executada. |
| NOME | String(100) | Sim | Nome completo por extenso. |
| NOMECRACHA | String(020) | Sim | Nome reduzido para impressão de Crachá. |
| POSSUICPF | String(003) | Sim | Informa se a pessoa física possui documento CPF. |
| CPF | Number(011,0) | Sim | Númedo do CPF da pessoa física. |
| TIPDOCIDE | String(003) | Sim | Tipo do documento de identidade  usuário. |
| DOCIDENTIDADE | String(020) | Sim | Número da identidade do usuário. |
| DATEXPIDE | String(010) | Sim | Data da expedição do documento de identidade. |
| ORGEXPIDE | String(010) | Sim | Órgão que expediu o documento de identidade. |
| CNH | String(020) | Sim | Número da CNH |
| VALIDADECNH | String(010) | Sim | Validade da carteira de CNH |
| NUMDOCOCO | String(020) | Sim | Documento referenciado no Termo de Ocorrência |
| RENAVAM | Number(011,0) | Sim | Número do renavam do veículo. |
| TIPOVEI | String(004) | Sim | Tipo do Veículo. |
| DESCRICAOTIPO | String(100) | Sim | Descrição do tipo do veículo. |
| MARCA | String(100) | Sim | Marca |
| MODELO | String(100) | Sim | Modelo |
| ANOFABRICACAO | Number(004,0) | Sim | Ano de fabricação do veículo. |
| CORPREDOMINANTE | String(100) | Sim | Cor predominante do veículo. |
| PLACA | String(100) | Sim | Placa do veículo. |
| REGISTROANTT | String(100) | Sim | Registro ANTT do veículo. |
| RETORNAVINCULO | String(003) | Sim | Retorna vínculo. |
| BIOMETRIA | String(018) | Sim | Biometria da mão do usuário. |
| DESCPLOCO | String(2000) | Sim | Descrição completa do Termo de Ocorrência. |
| CODTEROCO | Number(011,0) | Sim | Código do termo de ocorrência. |
| DATACORTE | String(010) | Sim | Data de corte para pesquisa de lista de liberação ou bloqueio |
| CODIGOCRACHA | String(020) | Sim | Número Físico do crachá emitido. |
| STATEROCO | String(003) | Sim | Status do Termo de Ocorrência. |
| SITCRA | String(003) | Sim | Situação do crachá. |
| DIRECAO | Number(001,0) | Sim | Direção da solicitação de processamento (0-Sistema p/BDCC, 1-BDCC p/ Sistema) |
| STAPRO | Number(001,0) | Sim | Status do processamento do registro sequencial. |
| AGUARDARET | String(003) | Sim | Aguarda Retorno |
| EMPRESA | Number(004,0) | Sim | Código da Empresa |
| TIPO | Number(001,0) | Sim | Tipo de Colaborador |
| CADASTRO | Number(009,0) | Sim | Cadastro |
| DATAINICIO | String(010) | Sim | Data Início Vínculo |
| DATAFIM | String(010) | Sim | Data Fim Vínculo |
| EMAIL | String(100) | Sim | Email |
| TIPOVIN | String(005) | Sim | Tipo de Vínculo |
| CNPJPROC | Number(015,0) | Sim | Cnpj Processo - Obsoleto |
| CfjPrc | String(014) | Sim | Cnpj Processo |
| TIPDOCOCO | String(007) | Sim | Tipo de Documento referenciado no Termo de Ocorrência |
| DESABROCO | String(200) | Sim | Descrição Abreviada do Termo de Ocorrência |
| DATAENVOCO | Date | Sim | Data de Envio do Termo de Ocorrência |
| HORAENVOCO | Number(005,0) | Sim | Hora de Envio do Termo de Ocorrência |
| EMPHARBOR | Number(004,0) | Sim | Número da empresa para conexão com o BDCC |
| FILHARBOR | Number(004,0) | Sim | Número da filial para conexão com o BDCC |
| SITUACAO | String(003) | Sim | Situação atual do cadastro da pessoa jurídica |
| CODREC | Number(003,0) | Sim | Código do Recinto Alfandegado |

---

## Chave Primária

- SEQUENCIAL

---

## Índices

### R873PROIndice2

**Tipo:** Não unico

Campos:
- TIPOREGISTRO

### R873PROIndice3

**Tipo:** Não unico

Campos:
- AGUARDARET

---

## Relacionamentos

Nenhum relacionamento cadastrado.
