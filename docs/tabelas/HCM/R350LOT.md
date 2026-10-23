# R350LOT

## Descrição

S-1020 - eSocial - Tabela de Lotações

---

## Resumo

- Campos: 40
- Chave Primária: 4 campo(s)
- Índices: 4
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IdeLot | String(030) | Não | Código atribuído pela empresa para a lotação |
| SeqLot | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| IniVal | Date | Sim | Data de início da validade das infomações prestadas no evento |
| FimVal | Date | Sim | Data final da Validade das  informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| TipLot | Number(002,0) | Sim | Código correspondente ao tipo de lotação |
| TipInL | Number(001,0) | Sim | Tipo de inscrição da lotação |
| CodFpa | Number(003,0) | Sim | Código relativo ao FPAS |
| CodTer | Number(004,0) | Sim | Código de terceiros |
| TerSus | Number(004,0) | Sim | Código de Terceiros Suspensos eSocial |
| TpInCo | Number(001,0) | Sim | Tipo de inscrição do contratante |
| InsCon | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjCon | String(014) | Sim | CNPJ Alfanumérico |
| TpInPr | Number(001,0) | Sim | Tipo de inscrição do propietário do CNO |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| EnvVal | String(001) | Sim | Envio é válido para o eSocial |
| GerLot | Number(001,0) | Sim | Geração Lotação |
| CodRat | Number(009,0) | Sim | Código do Rateio |
| CodFil | Number(006,0) | Sim | Código da Filial |
| CodOem | Number(008,0) | Sim | Código do Tomador de Serviço |
| IdeInt | Number(019,0) | Sim | Identificador |
| AliRat | Number(001,0) | Sim | Alíquota Definida no Decreto 3.048/99  Para a Atividade (CNAE) Predominante |
| FatFap | Number(005,4) | Sim | Fator Acidentário de Prevenção |
| NumInL | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjInL | String(014) | Sim | CNPJ Alfanumérico |
| InsPro | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjPro | String(014) | Sim | CNPJ Alfanumérico |

---

## Chave Primária

- NumEmp
- FilEmp
- IdeLot
- SeqLot

---

## Índices

### R350LOTIndice1

**Tipo:** Não unico

Campos:
- PidExc

### R350LOTIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- GerLot
- CodRat
- CodFil

### R350LOT_IDX_001

**Tipo:** Não unico

Campos:
- IdeInt

### R350LOT_IDX_002

**Tipo:** Não unico

Campos:
- NumEmp
- FilEmp
- CodRat
- CodFil
- GerLot

---

## Relacionamentos

Nenhum relacionamento cadastrado.
