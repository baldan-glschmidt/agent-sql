# E000PCD

## Descrição

Tabelas - Recebimento de Documentos Eletrônicos - Notas Fiscais de Entrada - Itens de Produto - Diversos

---

## Resumo

- Campos: 58
- Chave Primária: 1 campo(s)
- Índices: 3
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CgcFil | Number(015,0) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| DocIdeFil | String(014) | Sim | Número do cadastro nacional de pessoa jurídica da filial da empresa |
| CgcFor | Number(014,0) | Sim | Número do CNPJ ou CPF do fornecedor |
| DocIdeFor | String(014) | Sim | Número do CNPJ ou CPF do fornecedor |
| ChvNel | String(050) | Não | Chave de acesso da nota fiscal eletrônica |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| IndEsc | String(001) | Sim | Indicador de Produção em Escala Relevante |
| CodBnf | String(010) | Sim | Código de Benefício Fiscal na UF aplicado ao produto |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| IcmBfc | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza na UF de destino |
| BasFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza |
| AliFcp | Number(007,4) | Sim | Alíquota do ICMS para fundo de combate à pobreza |
| VlrFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza |
| BstFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido por substituição tributária |
| AstFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido por substituição tributária |
| VstFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido por substituição tributária |
| BreFcp | Number(015,2) | Sim | Base de cálculo do fundo de combate à pobreza retido ant. por subst. trib. |
| AreFcp | Number(007,4) | Sim | Alíquota do fundo de combate à pobreza retido anteriormente por subst. trib. |
| VreFcp | Number(015,2) | Sim | Valor do fundo de combate à pobreza retido anteriormente por subst. trib. |
| VicStd | Number(015,2) | Sim | Valor do ICMS-ST desonerado |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| VdiFcp | Number(015,2) | Sim | Valor diferido do ICMS relativo ao FCP |
| EfiFcp | Number(015,2) | Sim | Valor efetivo do ICMS relativo ao FCP |
| SeqNfi | Number(004,0) | Sim | Sequência do item na nota fiscal impressa |
| QtmBic | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico |
| VmoIcm | Number(015,2) | Sim | Valor do ICMS Monofásico |
| AliImo | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico |
| QtmBir | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Retido |
| VmoIcr | Number(015,2) | Sim | Valor do ICMS Monofásico Retido |
| AliImr | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Retido |
| QtmBif | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Diferido |
| VmoIcf | Number(015,2) | Sim | Valor do ICMS Monofásico Diferido |
| AliImf | Number(007,4) | Sim | Percentual de Diferimento do ICMS Monofásico |
| QtmBid | Number(015,4) | Sim | Quantidade da Base ICMS Monofásico Destacado |
| VmoIcd | Number(015,2) | Sim | Valor do ICMS Monofásico Destacado |
| AliImd | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Destacado |
| AliMor | Number(007,4) | Sim | Alíquota ad rem ICMS Monofásico Original |
| CbfRbc | String(010) | Sim | Código de Benefício Fiscal de redução de base de cálculo |
| StrOri | String(003) | Sim | Situação tributária Original do item da nota fiscal de entrada |
| SnfNfr | String(003) | Sim | Série da nota fiscal de entrada |
| ForNfr | Number(009,0) | Sim | Fornecedor da nota fiscal de entrada Ligada |
| NumNfr | Number(009,0) | Sim | Número da nota fiscal de entrada |
| SeqIpr | Number(003,0) | Sim | Sequência do item da nota fiscal de Entrada |
| CodInt | Number(002,0) | Sim | Código da integração |
| IdeExt | Number(009,0) | Sim | Número Identificador Externo |
| CtrExt | String(020) | Sim | Número do Contrato Externo |
| IdcExt | Number(009,0) | Sim | Código do Identificador do Contrato Externo |
| EmbExt | String(050) | Sim | Número do Embarque Externo |
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| IdeIpc | String(050) | Não | Identificador único alfanumérico |
| IndDev | String(001) | Sim | Indicativo se o item é uma devolução |
| CodNfc | String(007) | Sim | Código item cClass |

---

## Chave Primária

- IdeUni

---

## Índices

### E000PCDIndice1

**Tipo:** Não unico

Campos:
- DocIdeFil
- DocIdeFor
- ChvNel
- SeqIpc

### E000PCDIndice2

**Tipo:** Não unico

Campos:
- CgcFil
- CgcFor
- ChvNel
- SeqIpc

### E000PCDIndice3

**Tipo:** Não unico

Campos:
- IdeIpc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
