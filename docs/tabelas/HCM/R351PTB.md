# R351PTB

## Descrição

S-2500 - eSocial - Processo Trabalhista

---

## Resumo

- Campos: 38
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| IdeSeq | Number(005,0) | Não | Sequência parcial |
| SeqPtb | Number(009,0) | Não | Sequência |
| SeqTot | Number(005,0) | Sim | Soma das sequências parciais |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | Número de Inscrição |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipRes | Number(001,0) | Sim | Tipo de inscrição do contribuinte (responsável direto) |
| InsRes | Number(014,0) | Sim | Número de inscrição do contribuinte (responsável direto) - Obsoleto |
| CfjRes | String(014) | Sim | Número de inscrição do contribuinte (responsável direto) |
| OriPro | Number(001,0) | Sim | Origem do processo/demanda |
| ObsPro | String(999) | Sim | Observações relacionadas ao processo judicial ou à demanda submetida à CCP ou ao NINTER |
| DatSen | Date | Sim | Data da sentença ou da homologação do acordo do processo judicial |
| UfVara | String(002) | Sim | Unidade da Federação onde está localizada a Vara em que o processo tramitou |
| CodMun | Number(007,0) | Sim | Código do município, conforme tabela do IBGE |
| IdeVar | String(004) | Sim | Código de identificação da Vara em que o processo tramitou |
| DatCon | Date | Sim | Data da conciliação |
| CelAco | Number(001,0) | Sim | Âmbito de celebração do acordo |
| CnpjSi | Number(014,0) | Sim | CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER - Obsoleto |
| CfjSin | String(014) | Sim | CNPJ do sindicato representativo do trabalhador, no âmbito da CCP ou NINTER |
| NomTra | String(070) | Sim | Nome do trabalhador |
| DatNas | Date | Sim | Data de nascimento do trabalhador |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |
| AdmRes | Date | Sim | Data de admissão do trabalhador no estabelecimento responsável pelo pagamento |
| MatRes | String(030) | Sim | Matrícula atribuída ao trabalhador no estabelecimento responsável pelo pagamento |
| VlrPat | Number(014,2) | Sim | Valor total da cota patronal incidente sobre a remuneração paga ao trabalhador, que será objeto de requisição autônoma |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- CpfTra
- IdeSeq
- SeqPtb

---

## Índices

### R351PTBIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
