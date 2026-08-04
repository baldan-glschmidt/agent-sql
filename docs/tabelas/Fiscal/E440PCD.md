# E440PCD

## Descrição

Compras - Notas Fiscais de Entrada - Itens de Produto - Diversos

---

## Resumo

- Campos: 72
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqIpc | Number(003,0) | Não | Sequência do item na nota fiscal de entrada |
| IndEsc | String(001) | Sim | Indicador de Produção em Escala Relevante |
| CodBnf | String(010) | Sim | Código de Benefício Fiscal na UF aplicado ao produto |
| IntRe2 | String(001) | Sim | Registro Integrado para a EFD-Reinf no bloco 2 |
| IntRe4 | String(001) | Sim | Registro Integrado para a EFD-Reinf no bloco 4 |
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
| VlrBgi | Number(015,2) | Sim | Base de cálculo do GILRAT |
| PerGil | Number(004,2) | Sim | Percentual de GILRAT - Grau Incid. Incapac. Laborat. Decor. Riscos Amb. de Trab. |
| VlrGil | Number(015,2) | Sim | Valor do GILRAT |
| QtdRci | Number(014,5) | Sim | Quantidade retornada da compra em notas fiscais de retorno |
| CodDev | Number(012,0) | Sim | Código de Lançamento no SisDev |
| DatDev | Date | Sim | Data de Lançamento no SisDev |
| CanDev | String(100) | Sim | Motivo Cancelamento no SisDev |
| VicStd | Number(015,2) | Sim | Valor do ICMS-ST desonerado |
| MtdIst | Number(002,0) | Sim | Motivo desoneração ICMS-ST |
| PdiFcp | Number(007,2) | Sim | Percentual do diferimento de ICMS relativo ao FCP |
| VdiFcp | Number(015,2) | Sim | Valor diferido do ICMS relativo ao FCP |
| EfiFcp | Number(015,2) | Sim | Valor efetivo do ICMS relativo ao FCP |
| SeqNfi | Number(004,0) | Sim | Sequência do item na nota fiscal impressa |
| IdeExt | Number(009,0) | Sim | Número Identificador Externo |
| CtrExt | String(020) | Sim | Número do Contrato Externo |
| CodInt | Number(002,0) | Sim | Código da integração |
| IdcExt | Number(009,0) | Sim | Código do Identificador do Contrato Externo |
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
| AliFus | Number(005,2) | Sim | Percentual do FUST |
| BasFus | Number(015,2) | Sim | Base de Cálculo do FUST |
| VlrFus | Number(015,2) | Sim | Valor do FUST |
| AliFnt | Number(005,2) | Sim | Percentual do FUNTTEL |
| BasFnt | Number(015,2) | Sim | Base de Cálculo do FUNTTEL |
| VlrFnt | Number(015,2) | Sim | Valor do FUNTTEL |
| CodNfc | String(007) | Sim | Código item cClass |
| SnfNfr | String(003) | Sim | Série da nota fiscal de entrada Ligada |
| ForNfr | Number(009,0) | Sim | Fornecedor da nota fiscal de entrada Ligada |
| NumNfr | Number(009,0) | Sim | Número da nota fiscal de entrada Ligada |
| SeqIpr | Number(003,0) | Sim | Sequência do item da nota fiscal de Entrada Ligada |
| EmbExt | String(050) | Sim | Número do Embarque Externo |
| IndDev | String(001) | Sim | Indicativo se o item é uma devolução |
| VlrBcb | Number(015,4) | Sim | Valor da Base de Cálculo CBS/IBS Externo |

---

## Chave Primária

- CodEmp
- CodFil
- CodFor
- NumNfc
- CodSnf
- SeqIpc

---

## Índices

### E440PCDINDICE1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- CodDev

---

## Relacionamentos

Nenhum relacionamento cadastrado.
