# E044CCU

## Descrição

Cadastros - Centros de Custos

---

## Resumo

- Campos: 42
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodCcu | String(009) | Não | Código do centro de custos |
| DesCcu | String(080) | Não | Descrição do centro de custos |
| AbrCcu | String(020) | Não | Abreviatura do centro de custos |
| CodUsu | Number(010,0) | Sim | Código do usuário responsável pelo centro de custos |
| TipCcu | Number(001,0) | Não | Tipo do centro de custos |
| IndAgr | String(001) | Sim | Unidade de medida de tempo dos processos |
| CcuPai | String(009) | Sim | Código do centro de custos pai |
| AgrTax | String(010) | Sim | Código do agrupamento para geração de taxa única |
| MskCcu | String(040) | Sim | Máscara do centro de custos |
| ClaCcu | String(030) | Sim | Classificação do centro de custos |
| GruCcu | Number(001,0) | Sim | Grupo que o centro de custo pertence |
| NivCcu | Number(002,0) | Sim | Nível do centro de custos |
| PosCcu | Number(001,0) | Sim | Quantidade de posições do nível do centro de custos |
| AnaSin | String(001) | Sim | Indicativo se o centro de custos é analítico ou sintético |
| AceRat | String(001) | Sim | Indicativo se o centro de custos aceita lançamento de rateio |
| CriRat | Number(001,0) | Sim | Critério utilizado para rateio do centro de custos |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida - 1 |
| CtaRcr | Number(007,0) | Sim | Conta contábil reduzida - 2 |
| CtaFdv | Number(007,0) | Sim | Conta contábil reduzida - 3 |
| CtaFcr | Number(007,0) | Sim | Conta contábil reduzida - 4 |
| ClaDes | String(001) | Sim | Classificação de despesa |
| CodLoc | String(009) | Sim | Código da localização real do bem de acordo com o organograma |
| LocRea | String(025) | Sim | Localização real do bem de acordo com organograma |
| PlaSeg | String(003) | Sim | Código da localização na planta de seguro do bem |
| TaxIcu | Number(005,2) | Sim | Taxa de depreciação do bem para custos |
| CodTur | Number(002,0) | Sim | Código turno para acréscimo da depreciação |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| IntAgr | String(001) | Sim | Indicativo se o centro de custo integra com agronegócio |
| IntPos | String(001) | Sim | Indicativo se o registro integra no Gestão Safra |
| OriPos | String(001) | Sim | Indicativo se o registro é uma cultura de origem no Gestão Safra |
| USU_nomenc | String(030) | Sim | Nome Encarregado |
| USU_nomprd | String(040) | Sim | Nome utilizado producao |
| USU_dtpini | Date | Sim | Data Inicio producao |
| USU_dtpfim | Date | Sim | Data Fim producao |
| USU_EmUso | String(001) | Sim | Determina se o centro de custo esta valido. |
| USU_SeqImp | Number(003,0) | Sim | Sequência de impressão do centro de custo |
| USU_FORCOD | String(015) | Sim | Código Fornecedor PCP |
| USU_CcuDir | String(001) | Sim | Centro de Custo Nivel Diretor |

---

## Chave Primária

- CodEmp
- CodCcu

---

## Índices

### E044CCUIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- ClaCcu

---

## Relacionamentos

### IR_E044CCU_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

