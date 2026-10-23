# R351CON

## Descrição

S-2555 - Solicitação de Consolidação das Informações de Tributos Decorrentes de Processo Trabalhista

---

## Resumo

- Campos: 19
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| NumPro | String(020) | Não | Número do processo trabalhista, da ata ou número de identificação da conciliação |
| PerApu | Date | Não | Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença |
| SeqCon | Number(009,0) | Não | Sequência |
| SeqTot | Number(005,0) | Sim | Soma das sequências parciais |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Tipo de Ambiente eSocial |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Não | Tipo Inscrição |
| NumIns | Number(015,0) | Sim | Número de Inscrição - Obsoleto |
| CfjIns | String(014) | Sim | Número de Inscrição |
| PidExc | String(050) | Não | Identificador da pendência para execução |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- NumPro
- PerApu
- SeqCon

---

## Índices

### R351CONIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
