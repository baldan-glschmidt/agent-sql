# R350AMB

## Descrição

S-1060 - eSocial - Tabela de Ambientes de Trabalho (Obsoleto)

---

## Resumo

- Campos: 28
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumAmb | Number(007,0) | Não | Código do Ambiente de Trabalho |
| SeqAmb | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CodAmb | String(030) | Sim | Código do ambiente de trabalho do eSocial |
| NomAmb | String(100) | Sim | Nome do ambiente de trabalho |
| DscAmb | String(8000) | Sim | Descrição do ambiente de trabalho |
| LocAmb | Number(001,0) | Sim | Localização do ambiente de trabalho |
| TpInAm | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do ambiente de trabalho |
| NrInAm | Number(015,0) | Sim | Número de inscrição onde está situado o ambiente de trabalho |
| CodLot | String(030) | Sim | Código atribuído pela empresa para a lotação tributária |
| IniVal | Date | Sim | Data de início da validade das infomações prestadas no evento |
| FimVal | Date | Sim | Data final da validade das informações prestadas no evento |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações prestadas no evento |
| EnvVal | String(001) | Sim | Determina se envio é válido |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| IdeInt | Number(019,0) | Sim | Identificador |

---

## Chave Primária

- NumEmp
- FilEmp
- NumAmb
- SeqAmb

---

## Índices

### R350AMBIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
