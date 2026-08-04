# E070PEE

## Descrição

Ligação de produtos ou serviços por estado - Operações de entrada

---

## Resumo

- Campos: 21
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
| IcmInd | Number(005,2) | Sim | Percentual de ICMS interno especial para estado de destino |
| RedIcm | Number(008,5) | Sim | Percentual de redução da base de ICMS na UF de destino |
| TemIcm | String(001) | Sim | Indicativo se o produto ou serviço tributa ICMS na UF de destino |
| PerDfe | Number(007,4) | Sim | Percentual de diferimento do item de produto/serviço da nota fiscal de entrada |
| CodDfs | Number(006,0) | Sim | Código do dispositivo fiscal |
| AliFcp | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| IcmIne | Number(007,4) | Sim | Percentual de alíquota efetiva de ICMS interno para estado de destino |
| TipBdi | Number(002,0) | Sim | Tipo da base de cálculo do diferencial de alíquota do ICMS para compra de ativo imobilizado |
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

### E070PEEIndice1

**Tipo:** Não unico

Campos:
- SigUfs

---

## Relacionamentos

### IR_E070PEE_003

**Tabela:** E007UFS

| Origem | Destino |
|--------|---------|
| SigUfs | SigUfs |

