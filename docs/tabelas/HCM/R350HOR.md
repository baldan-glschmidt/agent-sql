# R350HOR

## Descrição

S-1050 - eSocial - Tabela de Horários/Turnos de Trabalho

---

## Resumo

- Campos: 27
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| HorEso | String(030) | Não | Código atribuído pelo empresa para o Horário Contratual |
| SeqHor | Number(009,0) | Não | Sequência |
| IdeInt | Number(009,0) | Sim | Identificador |
| CodEsc | Number(009,0) | Sim | Código da Escala |
| CodHor | Number(004,0) | Sim | Código do Horário |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| IniVal | Date | Sim | Data de início da validade das informações prestadas no evento |
| FimVal | Date | Sim | Data final da validade das informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| HorEnt | Number(004,0) | Sim | Hora de entrada |
| HorSai | Number(004,0) | Sim | Hora de saída |
| DurJor | Number(004,0) | Sim | Tempo de duração da jornada, em minutos |
| PerFex | String(001) | Sim | Permitir flexibilidade de horário |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- HorEso
- SeqHor

---

## Índices

### R350HORIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
