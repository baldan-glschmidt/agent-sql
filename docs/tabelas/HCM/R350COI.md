# R350COI

## Descrição

S-2260 - eSocial - Convocação para Trabalho Intermitente

---

## Resumo

- Campos: 36
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
| SeqCoi | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado |
| NumMat | String(030) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| CodCon | String(030) | Não | Código da Convocação |
| DatIni | Date | Sim | Data Início da Convocação |
| DatFim | Date | Sim | Data Fim da Convocação |
| DatPgt | Date | Sim | Data Prevista para Pagamento |
| CodHor | Number(004,0) | Sim | Código do Horário |
| DesJor | String(999) | Sim | Descrição da Jornada |
| IndLoc | Number(001,0) | Sim | Indidicativo do local de trabalho |
| TipLgr | String(005) | Sim | Tipo de Logradouro |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| NomBai | String(040) | Sim | Nome do Bairro |
| EndCep | Number(008,0) | Sim | CEP |
| CodCid | Number(007,0) | Sim | Cidade |
| CodEst | String(004) | Sim | Estado |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqCoi

---

## Índices

### R350COIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
