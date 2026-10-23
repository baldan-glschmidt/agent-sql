# R350PRO

## Descrição

S-1070 - eSocial - Tabela de Processos Administrativos/Judiciais

---

## Resumo

- Campos: 29
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| CodPro | Number(009,0) | Não | Número do Processo/Benefício |
| DatIni | Date | Não | Data Início |
| SeqPro | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| TipPro | Number(001,0) | Sim | Código Correspondente ao Tipo do Processo |
| NumPro | String(021) | Sim | Número do Processo Administrativo/Judicial |
| IniVal | Date | Sim | Data de Início da Validade das Informações Prestadas no Evento |
| FimVal | Date | Sim | Data Final da Validade das Informações |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| EstVar | String(002) | Sim | Identificação da UF da Seção Judiciária |
| CodMun | Number(007,0) | Sim | Código do Município |
| IdeVar | Number(004,0) | Sim | Código de Identificação da Vara |
| IndAut | Number(001,0) | Sim | Próprio Contribuinte ou Outra Entidade é o Autor da Ação |
| MatPro | Number(002,0) | Sim | Indicativo de matéria do processo ou alvará judicial |
| ObsPro | String(255) | Sim | Observação |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- CodPro
- DatIni
- SeqPro

---

## Índices

### R350PROIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
