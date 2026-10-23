# R350EEV

## Descrição

S-3000 - eSocial - Exclusão de Eventos

---

## Resumo

- Campos: 22
- Chave Primária: 7 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| TipEvt | String(006) | Não | Tipo de evento da exclusão |
| PerApu | Date | Não | Mês/Ano da folha de pagamento |
| SeqEev | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| NumRee | String(040) | Sim | Número do recibo do evento que será excluído |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| IndApu | Number(001,0) | Sim | Indicativo de período de apuração |
| PidOri | String(050) | Sim | Identificador do leiaute que deu origem à exclusão do S-1210 |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| LayOut | String(006) | Sim | Leiaute |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- TipEvt
- SeqEev
- PerApu

---

## Índices

### R350EEVIndice1

**Tipo:** Não unico

Campos:
- PidExc

### R350EEVIndice2

**Tipo:** Não unico

Campos:
- NumRee
- NumEmp

---

## Relacionamentos

Nenhum relacionamento cadastrado.
