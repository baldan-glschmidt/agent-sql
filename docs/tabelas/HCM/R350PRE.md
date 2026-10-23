# R350PRE

## Descrição

S-2190 - Registro Preliminar de Trabalhador

---

## Resumo

- Campos: 28
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| SeqAdm | Number(009,0) | Não | Sequência |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NomFun | String(040) | Sim | Nome do Colaborador |
| DatAdm | Date | Sim | Data de Admissão |
| DatNas | Date | Sim | Data de nascimento do trabalhador |
| MatTra | String(030) | Sim | Matrícula do Trabalhador |
| CodCat | Number(004,0) | Sim | Código da categoria |
| NatAti | Number(001,0) | Sim | Natureza da atividade |
| CodCbo | String(006) | Sim | Cbo 2002 do Cargo |
| SalFix | Number(014,2) | Sim | Salário fixo do trabalhador |
| UndFix | Number(001,0) | Sim | Unidade de pagamento da parte fixa da remuneração |
| TipCon | Number(001,0) | Sim | Tipo de contrato de trabalho |
| TerCon | Date | Sim | Data do Término do contrato |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvExc | String(001) | Sim | Exclusão realizada |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- SeqAdm

---

## Índices

### R350PREIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
