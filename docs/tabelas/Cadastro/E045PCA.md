# E045PCA

## Descrição

Tabelas - Plano Composição Auxiliar - Contas

---

## Resumo

- Campos: 19
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaAux | Number(009,0) | Não | Número reduzido da conta auxiliar |
| DesCta | String(200) | Não | Nomenclatura da conta auxiliar |
| AbrCta | String(020) | Não | Abreviatura da conta auxiliar |
| DefGru | String(001) | Não | Definição do grupo de conta auxiliar |
| MskAux | String(040) | Não | Máscara do grupo que a conta pertence |
| ClaAux | String(030) | Não | Classificação da conta auxiliar |
| GruAux | Number(001,0) | Não | Grupo que a conta auxiliar pertence |
| NivAux | Number(001,0) | Não | Nível da conta auxiliar |
| PosAux | Number(001,0) | Não | Quantidade de posições do nível da conta auxiliar |
| AnaSin | String(001) | Não | Indicativo se a conta auxiliar é sintética ou analítica |
| UltMov | Date | Sim | Data do último movimento da conta |
| SitAux | String(001) | Não | Situação da conta auxiliar |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatLig | Date | Sim | Data de ligação da conta auxiliar ao plano auxiliar da empresa |
| HorLig | Number(005,0) | Sim | Hora de ligação da conta contábil ao plano da empresa |
| UsuLig | Number(010,0) | Sim | Usuário de ligação da conta contábil ao plano da empresa |

---

## Chave Primária

- CodEmp
- CtaAux

---

## Índices

### E045PCAIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- ClaAux

### E045PCAIndice3

**Tipo:** Não unico

Campos:
- CodEmp
- SitAux
- ClaAux
- CtaAux

---

## Relacionamentos

Nenhum relacionamento cadastrado.
