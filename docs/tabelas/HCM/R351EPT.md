# R351EPT

## Descrição

S-3500 - eSocial - Exclusão de Eventos - Processo Trabalhista

---

## Resumo

- Campos: 19
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipEvt | String(006) | Não | Tipo de evento da exclusão |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| CpfTra | Number(011,0) | Não | Número do CPF do trabalhador |
| PerApu | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| SeqEpt | Number(009,0) | Não | Sequência |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Tipo de Ambiente eSocial |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Não | Tipo Inscrição |
| NumIns | Number(015,0) | Sim | Número de Inscrição - Obsoleto |
| CfjIns | String(014) | Sim | Número de Inscrição |
| PidOri | String(050) | Sim | Identificador do leiaute que deu origem à exclusão do S-2501 |
| PidExc | String(050) | Não | Identificador da pendência para execução |
| RecExc | String(040) | Sim | Número do recibo que será excluído |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| SeqPar | Number(005,0) | Sim | Sequência parcial |

---

## Chave Primária

- NumEmp
- FilEmp
- TipEvt
- NumPro
- CpfTra
- PerApu
- SeqEpt

---

## Índices

### R351EPTIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
