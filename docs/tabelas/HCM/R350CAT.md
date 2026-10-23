# R350CAT

## Descrição

S-2210 - eSocial - Comunicação de Acidente de Trabalho

---

## Resumo

- Campos: 73
- Chave Primária: 9 campo(s)
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
| DatAct | Date | Não | Data do Acidente |
| HorAct | Number(005,0) | Não | Hora do Acidente |
| DatCat | Date | Não | Data de registro da CAT |
| TipCat | Number(001,0) | Não | Tipo de CAT |
| SeqCat | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do empregador |
| NumIns | Number(014,0) | Sim | Número de inscrição do empregador - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição do empregador |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (Obsoleto) |
| NumMat | String(255) | Sim | Matrícula atribuída ao trabalhador |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| CodAct | String(006) | Sim | Tipo de acidente de trabalho (Obsoleto) |
| TipAci | Number(001,0) | Sim | Tipo de acidente de trabalho |
| HorTra | Number(005,0) | Sim | Horas trabalhadas antes do acidente |
| CatObt | String(001) | Sim | Houve óbito do trabalhador |
| DatObi | Date | Sim | Data do óbito do trabalhador |
| ComAut | String(001) | Sim | Houve comunicação à autoridade policial |
| SitGer | Number(009,0) | Sim | Código da situação geradora do acidente |
| IniCat | Number(001,0) | Sim | Iniciativa de emitir a CAT |
| ObsCat | String(999) | Sim | Observações da CAT |
| DatUlt | Date | Sim | Data do último Dia trabalhado |
| HouAfa | String(001) | Sim | Houve Afastamento |
| TipLoc | Number(001,0) | Sim | Tipo do Local do acidente |
| DesLoc | String(255) | Sim | Especificação do local do acidente |
| CodAmb | String(030) | Sim | Código do ambiente de trabalho no eSocial (Obsoleto) |
| TipLog | String(004) | Sim | Tipo de Logradouro |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| NomBai | String(090) | Sim | Nome do bairro/distrito |
| CodCep | Number(008,0) | Sim | Código de Endereçamento Postal |
| CodMun | Number(007,0) | Sim | Código do município |
| SigEst | String(002) | Sim | Sigla da Unidade da Federação |
| CodPai | Number(003,0) | Sim | Código do país |
| CodPst | String(012) | Sim | Código de Endereçamento Postal |
| TpInLo | Number(001,0) | Sim | Tipo de inscrição do local onde ocorreu o acidente ou doença ocupacional |
| CNPJLo | Number(014,0) | Sim | Número de inscrição do local onde ocorreu o acidente ou doença ocupacional - Obsoleto |
| CfjLoc | String(014) | Sim | Número de inscrição do local onde ocorreu o acidente ou doença ocupacional |
| CoCNES | String(007) | Sim | Código no Cadastro Nacional de Estabelecimento de Saúde (Obsoleto) |
| CodPar | Number(009,0) | Sim | Código correspondente à parte atingida |
| LatPar | Number(001,0) | Sim | Lateralidade da parte atingida |
| CodACa | Number(009,0) | Sim | Código correspondente ao agente causador do acidente |
| DatAte | Date | Sim | Data do atendimento |
| HorAte | Number(005,0) | Sim | Hora do atendimento |
| IndInt | String(001) | Sim | Indicativo de Internação |
| DurTra | Number(004,0) | Sim | Duração estimada do tratamento (em dias) |
| IndAfa | String(001) | Sim | Indicativo do afastamento |
| CodLes | Number(009,0) | Sim | Código da natureza da lesão |
| NatLes | String(200) | Sim | Descrição da natureza da lesão |
| DiaPro | String(100) | Sim | Diagnóstico Provável |
| CodCID | String(004) | Sim | Código da Classificação Internacional de Doenças |
| ObsAte | String(255) | Sim | Observação |
| NomMed | String(070) | Sim | Nome do médico/dentista que emitiu o atestado |
| IdeOrC | Number(001,0) | Sim | Órgão de classe do emitente |
| NumOrC | String(014) | Sim | Número de inscrição no órgão de classe |
| EstOrC | String(002) | Sim | Sigla da UF do órgão de classe |
| CatOri | String(040) | Sim | Número do recibo da CAT de origem |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |
| HrAcid | String(001) | Sim | Hora Acidente |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatAct
- HorAct
- DatCat
- SeqCat
- TipCat

---

## Índices

### R350CATIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
