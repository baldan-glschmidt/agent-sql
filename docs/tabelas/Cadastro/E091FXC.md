# E091FXC

## Descrição

Tabelas - Plano Financeiro - Relacionamento Contas X Centro de Custos Liberados

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CtaFin | Number(007,0) | Não | Conta Financeira |
| CodCcu | String(009) | Não | Código do centro de custos liberado |
| CriFxc | Number(001,0) | Não | Critério para relacionamento (1=Só ele, 2=Todas subordinadas a ele) |
| ObsFxc | String(250) | Sim | Observação do relacionamento |
| SitFxc | String(001) | Não | Situação do relacionamento |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |

---

## Chave Primária

- CodEmp
- CtaFin
- CodCcu

---

## Índices

### E091FXCIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodCcu

---

## Relacionamentos

### IR_E091FXC_001

**Tabela:** E091PLF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CtaFin | CtaFin |

### IR_E091FXC_002

**Tabela:** E044CCU

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodCcu | CodCcu |

