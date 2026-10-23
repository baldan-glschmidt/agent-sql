# R350STA

## Descrição

eSocial - Status de pendências

---

## Resumo

- Campos: 45
- Chave Primária: 1 campo(s)
- Índices: 9
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidExc | String(050) | Não | Identificador da pendência para execução |
| PidPen | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| DatHor | Number(014,6) | Sim | Data/Hora da geração da pendência |
| LayOut | String(006) | Sim | Leiaute que originou a pendência |
| NumRec | String(040) | Sim | Recibo de retorno |
| UsuRec | Number(010,0) | Sim | Usuário que gravou o recibo manualmente |
| DesRet | String(2000) | Sim | Descrição do retorno |
| DesRes | String(250) | Sim | Descrição do resumo |
| CodUsu | Number(010,0) | Sim | Usuário que originou a pendência |
| StaSit | Number(002,0) | Sim | Status Situação da Pendência |
| NumEmp | Number(004,0) | Sim | Abrangência Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Sim | Abrangência Tipo do Colaborador |
| NumCad | Number(009,0) | Sim | Abrangência Cadastro Colaborador |
| CodFil | Number(006,0) | Sim | Abrangência Filial |
| TabOrg | Number(004,0) | Sim | Abrangência Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Abrangência Local do Organograma |
| CodSit | Number(003,0) | Sim | Abrangência Código da Situação |
| CodEsc | Number(009,0) | Sim | Abrangência Código da Escala |
| CodCcu | String(018) | Sim | Abrangência Centro Custo |
| CodOem | Number(008,0) | Sim | Abrangência Código da Outra Empresa |
| EstSal | Number(004,0) | Sim | Abrangência Código da Última Estrutura Salarial |
| CodVin | Number(002,0) | Sim | Abrangência Código do Vínculo |
| TurInt | Number(001,0) | Sim | Abrangência Turno da Escala |
| TipAtn | Number(001,0) | Sim | Abrangência Tipo Atendido |
| CodExa | Number(004,0) | Sim | Abrangência Exames |
| EstCar | Number(004,0) | Sim | Abrangência Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Abrangência Código do Cargo |
| CodThp | Number(003,0) | Sim | Abrangência Tipo Hierarquia Posto |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| UltEnv | Number(014,6) | Sim | Data do Último Retorno |
| IniVal | Date | Sim | Data de Início da Validade do Envio no eSocial |
| CpfEmp | Number(015,0) | Sim | CPF/CNPJ Empregador |
| CfjIns | String(014) | Sim | CPF/CNPJ Empregador |
| PenExt | String(001) | Sim | Pendência gerada por uma alteração extemporânea |
| IdeAnt | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| PidOri | String(050) | Sim | Identificador do leiaute que deu origem à exclusão do S-1210 |
| InfFac | Number(001,0) | Sim | Informar se as informações facultativas devem ser enviadas para o eSocial |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| ClaEve | Number(001,0) | Sim | Classificação do evento |
| RunCnv | Number(001,0) | Sim | Desabilita trigger na conversão CNPJ alfanumérico. |

---

## Chave Primária

- PidExc

---

## Índices

### R350STAIndice1

**Tipo:** Não unico

Campos:
- DatHor

### R350STAIndice2

**Tipo:** Não unico

Campos:
- LayOut

### R350STAIndice3

**Tipo:** Não unico

Campos:
- NumRec

### R350STAIndice4

**Tipo:** Não unico

Campos:
- DesRet

### R350STAIndice5

**Tipo:** Não unico

Campos:
- DesRes

### R350STAIndice6

**Tipo:** Não unico

Campos:
- NumEmp
- PerApu
- IndApu
- LayOut

### R350STAIndice7

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- StaSit
- PenExt

### R350STAIndice8

**Tipo:** Não unico

Campos:
- PidExc
- NumRec

### R350STAIndice9

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
