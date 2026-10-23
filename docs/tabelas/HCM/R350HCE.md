# R350HCE

## Descrição

S-2231 - eSocial - Cessão/Exercício em Outro Órgão

---

## Resumo

- Campos: 26
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| DatIni | Date | Não | Data de início da Cessão |
| TipHce | Number(001,0) | Não | Tipo histórico da Cessão (Início ou Término) |
| SeqHce | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| MatTra | String(255) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| InsCes | Number(014,0) | Sim | CNPJ do empregador cessionário/destino |
| CfjCes | String(014) | Sim | CNPJ do empregador cessionário/destino |
| ResRem | String(001) | Sim | Empregador/órgão público declarante é responsável pela remuneração |
| DatTer | Date | Sim | Data de término da cessão |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatIni
- TipHce
- SeqHce

---

## Índices

### R350HCEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
