# R350POR

## Descrição

S-1080 - eSocial - Tabela de Operadores Portuários

---

## Resumo

- Campos: 27
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| SeqEst | Number(009,0) | Não | Sequência |
| CodFil | Number(006,0) | Sim | Código da Filial |
| CodOem | Number(008,0) | Sim | Código Outra Empresa |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CnpPor | Number(014,0) | Sim | CNPJ do Operador Portuário |
| CfjPor | String(014) | Sim | CNPJ do Operador Portuário |
| IniVal | Date | Sim | Data de Início da Validade das Informações Prestadas no Evento |
| FimVal | Date | Sim | Data Final da Validade das Informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| AplFap | String(001) | Sim | Aplica Fator FAP |
| AliRat | Number(001,0) | Sim | Alíquota Definida no Decreto 3.048/99  Para a Atividade (CNAE) Predominante |
| FatFap | Number(005,4) | Sim | Fator Acidentário de Prevenção |
| RatAju | Number(005,4) | Sim | Alíquota após ajustar pelo FAP |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute |
| LayOut | String(006) | Sim | Leiaute |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- SeqEst

---

## Índices

### R350PORIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
