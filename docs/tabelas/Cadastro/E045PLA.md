# E045PLA

## Descrição

Tabelas - Plano Contábil - Contas

---

## Resumo

- Campos: 30
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil |
| DesCta | String(250) | Não | Nomenclatura da conta contábil |
| AbrCta | String(020) | Não | Abreviatura da conta contábil |
| AceMan | String(001) | Não | Indicativo se a conta contábil aceita lançamentos manuais |
| DefGru | String(001) | Não | Definição do grupo de conta contábil |
| MskGcc | String(040) | Não | Máscara do grupo que a conta pertence |
| ClaCta | String(030) | Não | Classificação da conta contábil |
| GruCta | Number(001,0) | Não | Grupo que a conta contábil pertence |
| NivCta | Number(002,0) | Não | Nível da conta contábil |
| QtdPos | Number(001,0) | Não | Quantidade de posições do nível da conta contábil |
| CtaPar | Number(009,0) | Sim | Número da conta reduzida paralela |
| ClaPar | String(030) | Sim | Classificação paralela da conta contábil |
| DesPar | String(080) | Sim | Descrição paralela da conta contábil |
| AnaSin | String(001) | Não | Indicativo se a conta contábil é sintética ou analítica |
| NatCta | String(001) | Não | Indicativo se a natureza da conta contábil é credora ou devedora |
| ForRat | Number(001,0) | Sim | Código da forma de rateio |
| MetCon | Number(001,0) | Sim | Método de conversão da conta contábil |
| UltMov | Date | Sim | Data do último movimento da conta |
| CodNtg | Number(004,0) | Sim | Natureza de Gasto do custo ou despesa |
| SitCta | String(001) | Não | Situação da conta contábil |
| AplCta | String(001) | Sim | Indicador se a conta é utilizada para a gestão de patrimônio |
| ExiAux | String(001) | Sim | Indicativo se a conta exige ou não conta do plano auxiliar |
| DatLig | Date | Sim | Data de ligação da conta contábil ao plano da empresa |
| HorLig | Number(005,0) | Sim | Hora de ligação da conta contábil ao plano da empresa |
| UsuLig | Number(010,0) | Sim | Usuário de ligação da conta contábil ao plano da empresa |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| IntAgr | String(001) | Sim | Indicativo se a conta contábil integra com agronegócio |

---

## Chave Primária

- CodEmp
- CtaRed

---

## Índices

### E045PLAIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- ClaCta

---

## Relacionamentos

### IR_E045PLA_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

