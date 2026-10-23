# R083PLF

## Descrição

PPRA - Atual - Planos p/ Controle da Fonte Geradora

---

## Resumo

- Campos: 10
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 5

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Código de Atividades |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodFgl | Number(006,0) | Não | Código da Fonte Geradora |
| CodCau | Number(003,0) | Não | Causa da Exposição |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |
| SitFgl | String(001) | Sim | Situação da Fonte Geradora em Relação Plano de Ação |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- CodAgt
- CodFgl
- CodCau
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083PLF_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

### IR_R083PLF_005

**Tabela:** R083AGT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodGru | CodGru |
| CodAgt | CodAgt |

### IR_R083PLF_006

**Tabela:** R086FGL

| Origem | Destino |
|--------|---------|
| CodFgl | CodFgl |

### IR_R083PLF_007

**Tabela:** R086CAU

| Origem | Destino |
|--------|---------|
| CodCau | CodCau |

### IR_R083PLF_008

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

