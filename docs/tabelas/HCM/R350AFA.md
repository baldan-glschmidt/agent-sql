# R350AFA

## Descrição

S-2230 - eSocial - Afastamento Temporário

---

## Resumo

- Campos: 52
- Chave Primária: 8 campo(s)
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
| DatAfa | Date | Não | Data do Afastamento |
| HorAfa | Number(005,0) | Não | Hora do Afastamento |
| SecAfa | Number(001,0) | Não | Seção Layout Afastamento |
| SeqAfa | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| NumMat | String(255) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| CodMot | Number(002,0) | Sim | Código do motivo de afastamento temporário |
| TipAci | Number(001,0) | Sim | Tipo de Acidente de Trânsito |
| ObsIni | String(255) | Sim | Observações |
| IniPer | Date | Sim | Data de início do período aquisitivo de férias |
| FimPer | Date | Sim | Data de término do período aquisitivo de férias |
| CodCID | String(004) | Sim | Código de classificação internacional de doenças |
| QtdDia | Number(003,0) | Sim | Quantidade de dias de afastamento concedidos pelo médico |
| NomAte | String(070) | Sim | Nome do médico/dentista que emitiu o atestado |
| OrgCla | Number(001,0) | Sim | Número de Inscrição no Órgão de Classe |
| RegCon | String(014) | Sim | Registro no Conselho Profissional |
| EstCon | String(002) | Sim | Sigla da UF do órgão de classe |
| CNPJCe | Number(014,0) | Sim | CNPJ do órgão/entidade para o qual o trabalhador foi cedido |
| CfjCes | String(014) | Sim | CNPJ do órgão/entidade para o qual o trabalhador foi cedido |
| OnuCes | Number(001,0) | Sim | Ônus da Cessão |
| CNPJSi | Number(014,0) | Sim | CNPJ do Sindicato no qual o trabalhador exercerá o mandato |
| CfjSin | String(014) | Sim | CNPJ do Sindicato no qual o trabalhador exercerá o mandato |
| OnuSin | Number(001,0) | Sim | Trabalhador foi afastado com ônus ou sem ônus para a entidade sindical |
| ManCgc | Number(015,0) | Sim | CNPJ do órgão no qual o trabalhador exercerá o mandato eletivo |
| CfjMdt | String(014) | Sim | CNPJ do órgão no qual o trabalhador exercerá o mandato eletivo |
| ManRem | String(001) | Sim | Indicar se o servidor optou pela remuneração do cargo efetivo |
| MotAnt | Number(002,0) | Sim | Código do motivo anterior do afastamento temporário |
| OriMot | Number(001,0) | Sim | Origem do Motivo da Alteração |
| TipPJu | Number(001,0) | Sim | Tipo do Processo |
| NumPro | String(021) | Sim | Número do Processo Judicial referente à Origem do Motivo de Alteração |
| DatTer | Date | Sim | Data de término do afastamento |
| MotTer | Number(002,0) | Sim | Código do motivo de afastamento temporário |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |
| MsmMot | String(001) | Sim | Indica se o afastamento decorre de mesmo motivo de afastamento anterior |
| CatEso | Number(004,0) | Sim | Código da categoria atribuída ao trabalhador |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatAfa
- HorAfa
- SecAfa
- SeqAfa

---

## Índices

### R350AFAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
