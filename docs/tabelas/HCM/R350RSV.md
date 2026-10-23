# R350RSV

## Descrição

S-2399 - eSocial - Trabalhador Sem Vínculo de Emprego/Estatutário - Término

---

## Resumo

- Campos: 38
- Chave Primária: 5 campo(s)
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
| SeqRsv | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| IndGui | Number(001,0) | Sim | Indicativo do tipo de Guia |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| IndSeg | Number(001,0) | Sim | Indicador segmento e-social |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| MatTra | String(030) | Sim | Matrícula do Trabalhador |
| CodCat | Number(004,0) | Sim | Código da categoria |
| DatDes | Date | Sim | Data do Término para Informações do Trabalhador Avulso |
| MotDes | Number(002,0) | Sim | Motivo do desligamento do Diretor Não Empregado |
| PenAli | Number(001,0) | Sim | Indicativo de pensão alimentícia |
| PerAli | Number(005,2) | Sim | Percentual destinado ao alimentando |
| VlrAli | Number(014,2) | Sim | Valor destinado ao alimentando |
| NumPro | String(020) | Sim | Número do Processo Trabalhista Quando o Desligamento se Der Por Este Motivo |
| FimQua | Date | Sim | Data fim da quarentena |
| IndRem | Number(001,0) | Sim | Indicativo de situação de remuneração após o término |
| DatRem | Date | Sim | Data fim remuneração após o desligamento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| DatTer | Date | Sim | Data projetada para o término do aviso prévio indenizado |
| TipDem | Number(001,0) | Sim | Origem da demissão |
| DatPag | Date | Sim | Data de Pagamento |
| NovCPF | Number(011,0) | Sim | CPF do trabalhador |
| TemRcs | String(001) | Sim | Rescisão |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqRsv

---

## Índices

### R350RSVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
