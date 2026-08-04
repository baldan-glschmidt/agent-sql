# E012DPD

## Descrição

Cadastros - Famílias - Distribuição Proporcional por Derivações

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFam | String(006) | Não | Código da Família do produto |
| CodMdp | String(008) | Não | Código da máscara de derivações utilizada pela família de produtos |
| CodDer | String(007) | Não | Código da derivação do produto |
| DstPrp | Number(004,0) | Sim | Distribuição proporcional por derivação |
| SitDst | String(001) | Não | Código da Situação do Registro |

---

## Chave Primária

- CodEmp
- CodFam
- CodMdp
- CodDer

---

## Índices

### E012DPDIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodMdp
- CodDer

---

## Relacionamentos

### IR_E012DPD_001

**Tabela:** E012FAM

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFam | CodFam |

### IR_E012DPD_003

**Tabela:** E084CMD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMdp | CodMdp |
| CodDer | CodDer |

