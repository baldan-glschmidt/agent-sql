# R350FUN

## Descrição

S-1040 - eSocial - Tabela de Funções

---

## Resumo

- Campos: 25
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| SeqFun | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CodFun | String(030) | Sim | Código da função |
| IniVal | Date | Sim | Data de iniício da validade das informações prestadas no evento |
| FimVal | Date | Sim | Data final da validade das informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| DesFun | String(100) | Sim | Descrição da função |
| CodCbo | String(006) | Sim | Cbo 2002 do Cargo |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| IdeInt | Number(019,0) | Sim | Identificador |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- EstCar
- CodCar
- SeqFun

---

## Índices

### R350FUNIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

### IR_R350FUN_002

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R350FUN_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

