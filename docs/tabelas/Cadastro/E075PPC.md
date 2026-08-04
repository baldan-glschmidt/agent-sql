# E075PPC

## Descrição

Cadastros - Produtos - Ligação Produto/Derivação ao Cliente

---

## Resumo

- Campos: 62
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodCli | Number(009,0) | Não | Código do cliente relacionado ao produto |
| SigUfs | String(002) | Não | Sigla do estado da filial |
| CodTns | String(005) | Não | Código da transação |
| DesNfv | String(099) | Não | Descrição do produto para impressão na nota fiscal do cliente |
| UniMed | String(003) | Não | Código de Unidade de Medida do produto para o cliente - nota fiscal de saída |
| CodTst | String(003) | Sim | Código do tipo de ICMS substituído |
| CodClf | String(003) | Sim | Código interno da classificação fiscal do produto para o cliente |
| PerIpi | Number(008,4) | Sim | Percentual de IPI do produto válido para o cliente |
| TemIcm | String(001) | Sim | Indicativo se o produto tem ou não ICMS |
| CodStr | String(003) | Sim | Código da situação tributária |
| CodTic | String(003) | Sim | Código do ICMS Especial |
| CodTrd | String(003) | Sim | Código de redução de impostos |
| CodStp | String(003) | Sim | Código da substituição tributária do PIS |
| CodStc | String(003) | Sim | Código da substituição tributária do COFINS |
| ProCli | String(030) | Sim | Código do produto no cliente |
| CodBar | Number(014,0) | Sim | Código de barras do produto no cliente (EAN13) |
| ObsPpc | String(240) | Sim | Texto da observação da relação produto X cliente |
| TriPis | String(001) | Sim | Indicativo se o produto para o cliente tem tributação de PIS ou não |
| TriCof | String(001) | Sim | Indicativo se o produto para o cliente tem tributação de COFINS ou não |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| IndCdc | String(001) | Sim | Indicativo se considera este produto/derivação para o cliente no contrato tipo 8 |
| DscPrm | Number(008,5) | Sim | Percentual de desconto promocional |
| DscEsp | Number(008,5) | Sim | Percentual de desconto especial |
| DscExt | Number(008,5) | Sim | Percentual de desconto extra |
| AcrUni | Number(014,5) | Sim | Valor de acréscimo unitário |
| DstPrm | String(001) | Sim | Indicativo se destaca o desconto promocional no preço do item |
| DstExt | String(001) | Sim | Indicativo se destaca o desconto extra no preço do item |
| DstEsp | String(001) | Sim | Indicativo se destaca o desconto especial no preço do item |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da ligação Produto X Cliente |
| DatGer | Date | Sim | Data da geração |
| HorGer | Number(005,0) | Sim | Hora da geração |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| CodFif | String(010) | Sim | Código fiscal federal do produto |
| CodFie | String(060) | Sim | Código Fiscal Estadual |
| CodFim | String(010) | Sim | Código fiscal municipal do produto |
| CodFin | Number(004,0) | Sim | Código da finalidade de venda |
| IndPfs | String(001) | Sim | Indicativo se pode buscar os parâmetros fiscais da ligação Produto X Cliente |
| ConFin | String(001) | Sim | Consumidor final |
| MotDes | Number(002,0) | Sim | Motivo desoneração ICMS |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS |
| PerDif | Number(007,4) | Sim | Percentual de diferimento configurado a ligação de produto cliente |
| PerPif | Number(008,4) | Sim | Percentual do PIS de faturamento |
| PerCff | Number(008,4) | Sim | Percentual do COFINS de faturamento |
| TprIpi | String(004) | Sim | Código da tabela de tributação para o cálculo de IPI por unidade de medida |
| TprPis | String(004) | Sim | Código da tabela de tributação para o cálculo de PIS por unidade de medida |
| TprCof | String(004) | Sim | Código da tabela de tributação para o cálculo de COFINS por unidade de medida |
| EmiRec | String(001) | Sim | Emite receita agronômica |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| CodEnq | Number(003,0) | Sim | Código de enquadramento legal do IPI |
| QcoLot | String(001) | Sim | Utiliza quantidade comercial no Lote do XML da NF-e |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| CalFus | String(001) | Sim | Calcula FUST |
| AliFus | Number(005,2) | Sim | Percentual FUST |
| CalFnt | String(001) | Sim | Calcula FUNTTEL |
| AliFnt | Number(005,2) | Sim | Percentual FUNTTEL |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodCli
- SigUfs
- CodTns

---

## Índices

### E075PPCIndice1

**Tipo:** Não unico

Campos:
- CodCli

---

## Relacionamentos

### IR_E075PPC_001

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E075PPC_003

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

