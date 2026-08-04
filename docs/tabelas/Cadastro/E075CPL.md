# E075CPL

## Descrição

Cadastros - Produtos - Produtos Complementares

---

## Resumo

- Campos: 14
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePdc | Number(009,0) | Não | Número de identificação do registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do produto |
| ProCpl | String(014) | Não | Código do produto complementar |
| DerCpl | String(007) | Não | Código da derivação do produto complementar |
| QtdCpl | Number(014,5) | Sim | Quantidade nessária do produto complementar |
| SitPdc | String(001) | Sim | Situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- IdePdc

---

## Índices

### E075CPLCN_E075CPL

**Tipo:** Unico

Campos:
- CodEmp
- CodPro
- CodDer
- ProCpl
- DerCpl

### E075CPLIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- ProCpl
- DerCpl

---

## Relacionamentos

### IR_E075CPL_003

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

### IR_E075CPL_005

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| ProCpl | CodPro |
| DerCpl | CodDer |

