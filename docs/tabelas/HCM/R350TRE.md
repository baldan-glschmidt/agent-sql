# R350TRE

## Descrição

S-2245 - eSocial - Treinamentos, Capacitações e Exercícios Simulados (Obsoleto)

---

## Resumo

- Campos: 33
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqTre | Number(009,0) | Não | Sequência |
| CodCua | Number(009,0) | Não | Código do Curso |
| SeqHcr | Number(004,0) | Não | Sequência do Curso Aperfeiçoamento |
| DatNot | Date | Não | Data Anotação Registro |
| SeqNot | Number(002,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição (CNPJ/CPF) |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| NumMat | String(255) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| CodTce | Number(004,0) | Sim | Código do treinamento/capacitação/exercício simulado conforme tabela 29 |
| ObsTre | String(999) | Sim | Observação referente ao treinamento/capacitação/exercício simulado |
| DatTre | Date | Sim | Data de início do treinamento/capacitação/autorização/exercício simulado |
| DurTre | Number(006,2) | Sim | Duração do treinamento/capacitação/exercício simulado, em horas |
| ModTre | Number(001,0) | Sim | Modalidade do treinamento/capacitação/exercício simulado |
| TipTre | Number(001,0) | Sim | Tipo de treinamento/capacitação/exercício simulado |
| TreAnt | String(001) | Sim | Indicar se o treinamento ocorreu antes da admissão, em outro empregador |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqTre

---

## Índices

### R350TREIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
