# E059LPE

## Descrição

Tabelas - Ligação Produtos x Embalagens

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação |
| CodEmb | Number(004,0) | Não | Código da embalagem |
| UniLpe | String(003) | Sim | Código da unidade de medida para a quantidade máxima |
| QtdLpe | Number(014,5) | Sim | Quantidade máxima do produto/derivação para a embalagem |
| CpdLpe | Number(004,0) | Sim | Capacidade de empilhamento para a ligação produto x embalagem |
| SitLpe | String(001) | Não | Situação da ligação produto x embalagem |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| ImpEtq | String(001) | Sim | Indicativo se deve ser impressa a etiqueta na formação do volume |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodEmb

---

## Índices

### E059LPEIndice1

**Tipo:** Não unico

Campos:
- CodEmb

---

## Relacionamentos

### IR_E059LPE_003

**Tabela:** E059EMB

| Origem | Destino |
|--------|---------|
| CodEmb | CodEmb |

