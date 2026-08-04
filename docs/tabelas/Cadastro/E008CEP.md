# E008CEP

## Descrição

Tabelas - Cep

---

## Resumo

- Campos: 25
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CepIni | Number(008,0) | Não | Faixa inicial do CEP da cidade |
| CepFim | Number(008,0) | Não | Faixa final do CEP da cidade |
| CodFis | Number(007,0) | Sim | Número do código fiscal do município (escrita fiscal) |
| CodRai | Number(007,0) | Sim | Código da cidade para a RAIS |
| NomCid | String(060) | Não | Nome da cidade |
| SigUfs | String(002) | Não | Sigla do estado da cidade |
| CodTra | Number(009,0) | Sim | Código da transportadora padrão para a cidade |
| BaiCid | String(075) | Sim | Bairro referente ao CEP Informado (quando faixa de apenas um CEP) |
| EndCid | String(100) | Sim | Endereço referente ao CEP (quando faixa de apenas um CEP) |
| PerIss | Number(006,4) | Sim | Percentual do ISS previsto para venda dos serviços no município |
| ForIss | Number(009,0) | Sim | Código do fornecedor p/ geração do título de ISS |
| ImpIss | String(003) | Sim | Código do imposto para cálculo do vencimento de ISS |
| CepPol | Number(008,0) | Sim | CEP da Cidade Polo |
| DiaEnt | Number(002,0) | Sim | Quantidade de dias para a entrega neste CEP. Será somado a data base para cálculo do vencimento das parcelas da nota fiscal de saída e/ou pedido. |
| CodIbg | Number(007,0) | Sim | Código da cidade conforme a tabela do IBGE |
| CodDip | Number(007,0) | Sim | Código do município conforme a tabela da DIPJ |
| CodSia | Number(004,0) | Sim | Código do município do SIAFI |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| PerIsc | Number(006,4) | Sim | Percentual do ISS para o Simples Nacional |
| PerCol | Number(008,2) | Sim | Percentual de dispensa de coleta (I-Simp) |

---

## Chave Primária

- CepIni

---

## Índices

### E008CEPIndice1

**Tipo:** Não unico

Campos:
- SigUfs

### E008CEPIndice2

**Tipo:** Não unico

Campos:
- CepIni
- CepFim

---

## Relacionamentos

### IR_E008CEP_005

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

