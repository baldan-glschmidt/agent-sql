# R350EST

## Descrição

S-1005 - eSocial - Tabela de estabelecimentos e Obras de Construção Civil

---

## Resumo

- Campos: 44
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| SeqEst | Number(009,0) | Não | Sequência |
| CodFil | Number(006,0) | Sim | Código da Filial |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| TpInEs | Number(001,0) | Sim | Tipo de Inscrição do estabelecimento |
| InsEst | Number(014,0) | Sim | Número de inscrição do estabelecimento |
| CfjEst | String(014) | Sim | Número de inscrição do estabelecimento |
| IniVal | Date | Sim | Data de início da validade das informações prestadas no evento |
| FimVal | Date | Sim | Data final da validade das informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| CodCna | Number(007,0) | Sim | Código do CNAE 2.0 |
| AliRat | Number(001,0) | Sim | Alíquota definida no decreto 3.048/99 para a atividade (CNAE) preponderante |
| FatFap | Number(006,4) | Sim | Fator acidentário de prevenção |
| RatAju | Number(005,4) | Sim | Alíquota após ajuste pelo FAP |
| TipPrR | Number(001,0) | Sim | Tipo Processo RAT |
| NumPrR | String(020) | Sim | Número Processo RAT |
| CodSuR | Number(014,0) | Sim | Código Indicativo Suspensão Rat |
| TipPrF | Number(001,0) | Sim | Tipo Processo FAP |
| NumPrF | String(020) | Sim | Número Processo FAP |
| CodSuF | Number(014,0) | Sim | Código Indicativo Suspensão FAP |
| TipCae | Number(001,0) | Sim | Tipo do CAEPF |
| IndSub | Number(001,0) | Sim | Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil |
| RegPon | Number(001,0) | Sim | Forma de Registro do Ponto |
| ConApr | Number(001,0) | Sim | Indicativo de Contratação de Aprendiz |
| ProEEd | String(020) | Sim | Número do processo de dispensa |
| EntEEd | String(001) | Sim | Entidade Educativa/Prática Desportiva |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| EnvVal | String(001) | Sim | Determina se envio é válido |
| ConPcd | Number(002,0) | Sim | Indicativo de Contratação de PCD(Pessoa com deficiência) |
| ProPCD | String(020) | Sim | Número do processo de PCD |
| CnpRes | Number(015,0) | Sim | Preencher com o CNPJ responsável pela inscrição no cadastro de obras da RFB |
| CfjRes | String(014) | Sim | Preencher com o CNPJ responsável pela inscrição no cadastro de obras da RFB |

---

## Chave Primária

- NumEmp
- FilEmp
- SeqEst

---

## Índices

### R350ESTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
