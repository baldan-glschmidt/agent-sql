# E043PCM

## Descrição

Tabelas - Modelos de Planos - Contas ou Centros de Custos

---

## Resumo

- Campos: 34
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| CtaRed | Number(009,0) | Não | Número reduzido da conta do modelo de plano |
| MskGcc | String(040) | Não | Máscara do grupo que a conta pertence |
| DefGru | String(001) | Não | Definição da conta |
| ClaCta | String(030) | Não | Classificação da conta do modelo de plano |
| DesCta | String(250) | Não | Nomenclatura da conta do modelo de plano |
| AbrCta | String(020) | Não | Abreviatura da conta do modelo de plano |
| AnaSin | String(001) | Não | Indicativo se a conta é analítica ou sintética |
| NatCta | String(001) | Não | Indicativo se a natureza da conta é credora ou devedora |
| NivCta | Number(002,0) | Não | Nível da conta do modelo de plano |
| ExiRat | String(001) | Não | Indicativo se a conta exige ou não rateio gerencial |
| ForRat | Number(001,0) | Não | Forma de rateio da conta do modelo de plano |
| CtaPar | Number(009,0) | Sim | Número da conta reduzida paralela |
| ClaPar | String(030) | Sim | Classificação paralela da conta contábil |
| DesPar | String(080) | Sim | Descrição paralela da conta contábil |
| ModCtb | Number(004,0) | Sim | Código do modelo do plano contábil |
| CtaCtb | Number(007,0) | Sim | Conta contábil reduzida relacionada a conta financeira |
| CodCcu | String(009) | Sim | Código do centro de custos sugerido para modelos tipo 3 = Centro Custos |
| TipCcu | Number(001,0) | Sim | Tipo do centro de custos |
| ExiAux | String(001) | Sim | Indicativo se a conta exige ou não conta do plano composição auxiliar |
| MetCon | Number(001,0) | Sim | Método de conversão da conta contábil |
| ValIni | Date | Sim | Data de validade inicial da conta |
| ValFin | Date | Sim | Data de validade final da conta |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| AtrCtb | String(200) | Sim | Atributo da conta |
| ColCtb | String(200) | Sim | Coluna da conta |
| CtbHom | String(001) | Sim | Conta homologada |
| IntPos | String(001) | Sim | Indicativo se o registro integra no Gestão Safra |
| CosAti | String(001) | Sim | Conta COSIF de Ativo (TJEO) |

---

## Chave Primária

- CodMpc
- CtaRed

---

## Índices

### E043PCMIndice2

**Tipo:** Não unico

Campos:
- CodMpc
- CodCcu

---

## Relacionamentos

### IR_E043PCM_000

**Tabela:** E043MPC

| Origem | Destino |
|--------|---------|
| CodMpc | CodMpc |

