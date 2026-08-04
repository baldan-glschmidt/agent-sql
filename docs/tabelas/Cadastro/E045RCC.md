# E045RCC

## Descrição

Tabelas - Plano Contábil - Relacionamento com Centros de  Custos

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 2
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRcc | Number(003,0) | Não | Código do relacionamento entre plano contábil e centro de custos |
| DesRcc | String(040) | Não | Descrição do relacionamento entre conta X centro de custos |
| CtaRed | Number(007,0) | Não | Conta contábil reduzida relacionada ao centro de custos |
| CtaRe2 | Number(007,0) | Sim | Conta contábil reduzida 2 relacionada ao centro de custos |
| CtaRe3 | Number(007,0) | Sim | Conta contábil reduzida 3 relacionada ao centro de custos |
| CodCcu | String(009) | Não | Código do centro de custos relacionado a conta contábil |
| MskRes | String(250) | Sim | Máscara resultante para inversão gerencial |
| ObsRcc | String(250) | Sim | Observação do relacionamento |

---

## Chave Primária

- CodEmp
- CodRcc

---

## Índices

### E045RCCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CtaRed

### E045RCCIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodCcu

---

## Relacionamentos

### IR_E045RCC_003

**Tabela:** E045PLA

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaRed | CtaRed |

### IR_E045RCC_006

**Tabela:** E044CCU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCcu | CodCcu |

