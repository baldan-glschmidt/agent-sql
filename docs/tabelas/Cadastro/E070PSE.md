# E070PSE

## Descrição

Ligação de produtos ou serviços por estado - Operações de saída

---

## Resumo

- Campos: 24
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| DatIni | Date | Não | Data de início da vigência |
| SigUfs | String(002) | Não | Sigla do estado |
| CodPro | String(014) | Não | Código do produto |
| CodSer | String(014) | Não | Código do serviço |
| AliFcp | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza |
| UsuGer | Number(009,0) | Sim | Usuário responsável pela geração do cadastro |
| DatGer | Date | Sim | Data da geração do cadastro |
| HorGer | Number(005,0) | Sim | Hora/minuto da geração do cadastro |
| UsuAtu | Number(009,0) | Sim | Usuário responsável pela última atualização do cadastro |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| IcmInd | Number(005,2) | Sim | Percentual de ICMS interno especial para estado de destino |
| RedIcm | Number(008,5) | Sim | Percentual de redução da base de ICMS na UF de destino |
| TemIcm | String(001) | Sim | Indicativo se o produto ou serviço tributa ICMS na UF de destino |
| CodBic | String(003) | Sim | Código da modalidade da base de cálculo do ICMS na UF de destino |
| PerDfs | Number(007,4) | Sim | Percentual de diferimento do item de produto/serviço da nota fiscal de saída |
| PerDfe | Number(007,4) | Sim | [INUTILIZADO] - Percentual de diferimento do item de produto/serviço da nota fiscal de entrada |
| RedAli | String(001) | Não | Indicativo se a redução da base de ICMS é aplicada na alíquota de ICMS da origem |
| BicInt | String(001) | Não | Indicativo se considera a base de ICMS da origem integral ou com redução |
| StIcmS | String(003) | Sim | Código da situação tributária para saídas do produto/Serviço |
| PerRbd | Number(007,4) | Sim | Percentual de Redução de Base DIFAL |

---

## Chave Primária

- CodEmp
- CodFil
- DatIni
- SigUfs
- CodPro
- CodSer

---

## Índices

### E070PSEIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E070PSE_003

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

